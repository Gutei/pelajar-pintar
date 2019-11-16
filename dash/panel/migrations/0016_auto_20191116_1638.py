# Generated by Django 2.1.7 on 2019-11-16 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0015_schoolmagazine_schoolmagazineactivity'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolmagazine',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='schoolmagazine',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]