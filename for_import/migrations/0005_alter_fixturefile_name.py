# Generated by Django 4.0.1 on 2022-07-30 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('for_import', '0004_alter_fixturefile_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixturefile',
            name='name',
            field=models.CharField(default='NON', max_length=1000, verbose_name='название фстуры'),
        ),
    ]
