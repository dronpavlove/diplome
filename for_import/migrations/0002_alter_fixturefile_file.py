# Generated by Django 4.0.1 on 2022-07-28 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('for_import', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixturefile',
            name='file',
            field=models.FileField(upload_to='admin_fixtures', verbose_name='файл фикстур'),
        ),
    ]
