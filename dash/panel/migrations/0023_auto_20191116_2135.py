# Generated by Django 2.1.7 on 2019-11-16 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0022_school_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='level',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'TK'), (1, 'PAUD'), (2, 'SD'), (3, 'MI'), (4, 'SMP'), (5, 'MTs'), (6, 'SMA'), (7, 'SMK'), (8, 'MA')], null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='type',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Negeri'), (1, 'Swasta')], null=True),
        ),
    ]
