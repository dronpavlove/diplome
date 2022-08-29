# Generated by Django 4.0.1 on 2022-07-13 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientproductview',
            options={'ordering': ('-created_dt',)},
        ),
        migrations.AddField(
            model_name='client',
            name='full_address',
            field=models.TextField(blank=True, null=True, verbose_name='Полный адрес'),
        ),
        migrations.AddField(
            model_name='client',
            name='orders',
            field=models.ManyToManyField(related_name='orders', to='orders.Order', verbose_name='Заказы'),
        ),
        migrations.AddField(
            model_name='clientproductview',
            name='created_dt',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='city',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='город'),
        ),
        migrations.AlterField(
            model_name='client',
            name='street',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='улица'),
        ),
    ]