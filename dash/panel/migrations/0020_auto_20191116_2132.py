# Generated by Django 2.1.7 on 2019-11-16 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0019_city_province'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='panel.City'),
        ),
        migrations.AddField(
            model_name='school',
            name='province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='panel.Province'),
        ),
    ]
