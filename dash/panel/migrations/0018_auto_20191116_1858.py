# Generated by Django 2.1.7 on 2019-11-16 11:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0017_province'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('code', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'cities',
            },
        ),
        migrations.AlterModelTable(
            name='province',
            table='provinces',
        ),
    ]
