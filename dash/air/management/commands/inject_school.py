import requests
from django.core.management.base import BaseCommand, CommandError
from panel.models import City, School, Province


class Command(BaseCommand):
    def add_arguments(self, parser):
        """
        Positional arguments
        jenjang = sd, smp, sma, smk

        """
        parser.add_argument('jenjang', nargs='+', type=str)

    def handle(self, *args, **options):

        kab = City.objects.all()
        jenjang = options.get('jenjang')

        for k in kab:
            c = requests.get('http://jendela.data.kemdikbud.go.id/api/index.php/Csekolah/detailSekolahGET?mst_kode_wilayah={}&bentuk={}'.format(k.code, jenjang[0]))
            data = c.json().get('data')

            for d in data:
                prov_code = d['kode_prop'].strip()
                city_code = d['kode_kab_kota'].strip()
                prov = Province.objects.filter(code=prov_code).first()
                city = City.objects.filter(code=city_code).first()

                if jenjang[0] == 'sd':
                    lvl = 2
                elif jenjang[0] == 'smp':
                    lvl = 4
                elif jenjang[0] == 'sma':
                    lvl = 6
                else:
                    lvl = 7

                sch = School(school_number=d['npsn'],
                             name=d['sekolah'],
                             type=0 if d['status'] == "N" else 1,
                             level=lvl,
                             province=prov,
                             city=city,
                             address=d['alamat_jalan'] + ' ' + d['kecamatan'],
                             lat=d['lintang'],  # garis lintang
                             lng=d['bujur'],  # bujur
                             )
                sch.save()
