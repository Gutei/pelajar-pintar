import requests
from django.core.management.base import BaseCommand, CommandError
from panel.models import City, School, Province


class Command(BaseCommand):

    def handle(self, *args, **options):

        kab = City.objects.all()
        jenjang = ['sd', 'smp', 'sma', 'smk']
        # print(data[1]['kode_wilayah'])
        # print(dir(c.json()))
        # for d in c.json().get('data'):
        #

        for j in jenjang:
            for k in kab:
                print(k.code)
                print(j)
                c = requests.get('http://jendela.data.kemdikbud.go.id/api/index.php/Csekolah/detailSekolahGET?mst_kode_wilayah={}&bentuk={}'.format(k.code, j))
                data = c.json().get('data')

            for d in data:
                prov = Province.objects.filter(code=d['kode_prop']).first()
                city = City.objects.filter(code=d['kode_kab_kota']).first()
                TYPE = 0 if d['status'] == 'N' else TYPE = 1
                if j == 'sd':
                    lvl = 2
                elif j == 'smp':
                    lvl = 4
                elif j == 'sma':
                    lvl = 6
                else:
                    lvl = 7
                sch = School(school_number=d['npsn'],
                             name=d['sekolah'],
                             type=TYPE,
                             level=lvl,
                             province=prov,
                             city=city,
                             address=d['alamat_jalan'] + ' ' + d['kecamatan'],
                             lat=d[''],
                             lng=d[''],
                             )
                sch.save()
