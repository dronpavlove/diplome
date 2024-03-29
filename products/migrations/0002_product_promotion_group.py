# Generated by Django 4.0.1 on 2022-07-10 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='promotion_group',
            field=models.ForeignKey(blank=True, default=None, help_text='Товар может входить в группу товаров со скидкой. В этом случае на каждый товар в группе действует определенная скидка', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='products', related_query_name='product', to='promotions.promotiongroup', verbose_name='скидочная группа товаров'),
        ),
    ]
