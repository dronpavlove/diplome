# Generated by Django 4.0.1 on 2022-07-10 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Promotions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=39, verbose_name='название')),
                ('description', models.TextField(blank=True, default='', max_length=500, verbose_name='описание')),
                ('discount', models.FloatField(default=0, verbose_name='скидка, %')),
            ],
            options={
                'verbose_name': 'скидка',
                'verbose_name_plural': 'скидки',
            },
        ),
        migrations.CreateModel(
            name='PromotionGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='название группы')),
                ('promotion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promotion_groups', related_query_name='promotion_group', to='promotions.promotions', verbose_name='скидка')),
            ],
            options={
                'verbose_name': 'группа товаров со скидкой',
                'verbose_name_plural': 'группы товаров со скидкой',
            },
        ),
    ]
