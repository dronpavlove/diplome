# Generated by Django 4.0.1 on 2022-07-04 13:54

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postcode', models.IntegerField(blank=True, null=True, verbose_name='почтовый индекс')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='accounts/', verbose_name='фотография')),
                ('phone', models.CharField(max_length=16, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='Введите корректный номер, без пробелов (+79999999999)', regex='^\\+?7?\\d{8,15}$')], verbose_name='контактный номер')),
                ('city', models.CharField(blank=True, max_length=256, verbose_name='город')),
                ('street', models.CharField(blank=True, max_length=256, verbose_name='улица')),
                ('house_number', models.IntegerField(blank=True, null=True, verbose_name='номер дома')),
                ('apartment_number', models.IntegerField(blank=True, null=True, verbose_name='номер квартиры')),
                ('spent_money', models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='потратил денег')),
                ('is_seller', models.BooleanField(default=False, verbose_name='продавец')),
                ('patronymic', models.CharField(default='', error_messages={'max_length': 'Слишком длинное Отчество!'}, max_length=50, verbose_name='Отчество')),
                ('limit_items_views', models.IntegerField(blank=True, default=20, help_text='Тут можно изменить это значение, по умолчанию 20 минимум 4.', validators=[django.core.validators.MinValueValidator(4)], verbose_name='Сколько максимум показывать товаров')),
                ('item_in_page_views', models.IntegerField(blank=True, default=8, error_messages={'min_length': 'Не стоит устанавливать меньше 2!'}, help_text='По сколько товаров будет добавляться при нажатии на кнопку "показать еще", но не больше чем разрешено', validators=[django.core.validators.MinValueValidator(2)], verbose_name='По сколько товаров выводить на странице')),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
                'db_table': 'Client',
            },
        ),
        migrations.CreateModel(
            name='ClientProductView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_products_view', related_query_name='client_products_views', to='accounts.client')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_products_view', related_query_name='client_products_views', to='products.product')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.AddField(
            model_name='client',
            name='item_view',
            field=models.ManyToManyField(blank=True, through='accounts.ClientProductView', to='products.Product', verbose_name='Товары, которые смотрел пользователь'),
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
    ]
