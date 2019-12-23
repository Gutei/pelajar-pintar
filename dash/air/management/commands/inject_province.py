import requests
from django.core.management.base import BaseCommand, CommandError
from panel.models import Province


class Command(BaseCommand):

    def handle(self, *args, **options):

        province = Province.objects.all().count()

        if province > 0:
            Province.objects.all().delete()

        c = requests.get('http://jendela.data.kemdikbud.go.id/api/index.php/cwilayah/wilayahGet')
        data = c.json().get('data')
        # print(data[1]['kode_wilayah'])
        # print(dir(c.json()))
        # for d in c.json().get('data'):
        #
        for d in data:
            prov = Province(code=d['kode_wilayah'], name=d['nama'])
            prov.save()