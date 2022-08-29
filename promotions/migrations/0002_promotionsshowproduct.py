# Generated by Django 4.0.1 on 2022-08-11 14:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_productphoto_photo'),
        ('promotions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PromotionsShowProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limit_day_show_product', models.PositiveSmallIntegerField(blank=True, default=1, error_messages={'max_value': 'Значение не больше 20'}, validators=[django.core.validators.MaxValueValidator(20)], verbose_name='Сколько дней показывать товар дня')),
                ('product_show', models.ForeignKey(blank=True, help_text='выберите товар, который будет показан как товар дня', null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='товар дня')),
            ],
            options={
                'verbose_name': 'Товар дня - настройка',
                'verbose_name_plural': 'Товары дня - настройка',
            },
        ),
    ]