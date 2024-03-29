# Generated by Django 4.0.1 on 2022-07-25 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0002_alter_shopphoto_options_alter_shopproduct_options_and_more'),
        ('basket', '0002_alter_basketitem_options_basketitem_old_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basketitem',
            name='seller',
        ),
        migrations.AddField(
            model_name='basketitem',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='basket_items', to='shops.shops', verbose_name='Магазин-продавец'),
        ),
        migrations.AddField(
            model_name='basketitem',
            name='shop_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='basket_items', to='shops.shopproduct'),
        ),
    ]
