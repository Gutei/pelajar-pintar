# Generated by Django 2.1.7 on 2019-11-16 08:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0013_auto_20191116_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='abstractschool',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
