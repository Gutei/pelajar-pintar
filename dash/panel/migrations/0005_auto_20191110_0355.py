# Generated by Django 2.1.7 on 2019-11-09 20:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0004_auto_20191110_0354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='id',
            field=models.UUIDField(default=uuid.UUID('64babcc4-b687-4cba-a6c9-99d33b52ff95'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='schoolachievement',
            name='id',
            field=models.UUIDField(default=uuid.UUID('aedcb811-e233-46c7-baa6-de0ea69d0c80'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='schoolactivity',
            name='id',
            field=models.UUIDField(default=uuid.UUID('5f081e6d-ab1c-4364-8d1e-5f28c0d2651d'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='schoolcontact',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ef40391b-b779-4d9a-823e-f160b39852e5'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='schoolextracurricular',
            name='id',
            field=models.UUIDField(default=uuid.UUID('cd37ec65-0e7b-4af3-8158-5bbabccd9296'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='schoolmajor',
            name='id',
            field=models.UUIDField(default=uuid.UUID('4f229913-3dd0-4504-841f-8b26c7955c3a'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='id',
            field=models.UUIDField(default=uuid.UUID('5ff9c5a4-8d53-41cb-9992-d571ad9ddc6a'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='teachercontact',
            name='id',
            field=models.UUIDField(default=uuid.UUID('3254f528-d8c9-40f9-873c-877218991ff0'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
