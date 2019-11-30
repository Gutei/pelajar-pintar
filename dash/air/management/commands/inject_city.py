import requests
from django.core.management.base import BaseCommand, CommandError
from panel.models import Province, City


class Command(BaseCommand):

    def handle(self, *args, **options):

        city = City.objects.all().count()

        if city > 0:
            return None

        province = Province.objects.all()

        for p in province:
            province_code = p.code
            c = requests.get('https://x.rajaapi.com/MeP7c5ne7f0iqtLj3LSaZG9R1GgSziHYVW24b3tVKnSG39B6fZaUw9VLxO/m/wilayah/kabupaten?idpropinsi={}'.format(province_code))
            # print(c.json().get('data'))
            # print(dir(c.json()))
            for d in c.json().get('data'):
                data = City(province=p, code=d.get('id'), name=d.get('name'))
                data.save()
                print(d)
