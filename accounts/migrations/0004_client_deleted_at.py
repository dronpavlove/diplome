# Generated by Django 4.0.1 on 2022-08-17 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_client_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
    ]