import requests
from django.core.management.base import BaseCommand, CommandError
from panel.models import Province, City


class Command(BaseCommand):

    def handle(self, *args, **options):

        city = City.objects.all().count()

        if city > 0:
            City.objects.all().delete()

        c = requests.get("http://jendela.data.kemdikbud.go.id/api/index.php/cwilayah/wilayahKabGet")
        # print(c.json().get('data'))
        data = c.json().get('data')
        # print(dir(c.json()))
        for d in data:
            mst_kode = d['mst_kode_wilayah'].strip()
            kode = d['kode_wilayah'].strip()
            prov = Province.objects.filter(code=mst_kode).first()
            data = City(code=kode, name=d['nama'], province=prov)
            data.save()
