# Generated by Django 2.1.7 on 2019-11-16 08:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('panel', '0012_schooltoken_studentregistrationtoken'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractSchool',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'abstract_schools',
            },
        ),
        migrations.AddField(
            model_name='school',
            name='level',
            field=models.CharField(blank=True, choices=[(0, 'TK'), (1, 'PAUD'), (2, 'SD'), (3, 'MI'), (4, 'SMP'), (5, 'MTs'), (6, 'SMA'), (7, 'SMK'), (8, 'MA')], max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='abstractschool',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='panel.School'),
        ),
        migrations.AddField(
            model_name='abstractschool',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
