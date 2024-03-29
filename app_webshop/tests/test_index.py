from django.conf import settings
from django.db import models
from django.test import TestCase
from django.urls import reverse

from promotions.models import Promotions, PromotionGroup
from shops.models import Shops, ShopProduct
from products.models import Category, Product
from ..views import Index


settings.DEBUG = False
try:
    settings.MIDDLEWARE.remove("debug_toolbar.middleware.DebugToolbarMiddleware")
except ValueError:
    pass


class TestIndex(TestCase):
    """
    Тестирование главной страницы.
    """

    @classmethod
    def setUpTestData(cls):
        # магазин
        shop = Shops.objects.create(
            name="Тестовый магазин",
            city="city", street="street",
            phone="123", email="test@test.com",
        )

        # категория товаров
        cls.category = Category.objects.create(
            category_name="Тестовые товары",
        )

        # скидки
        cls.promo10 = Promotions.objects.create(
            name="Минус 10%",
            discount=10,
        )
        cls.promo_group = PromotionGroup.objects.create(
            name="Группа тестовых товаров",
            promotion=cls.promo10,
        )

        # товары
        cls.products_count = 6
        for i in range(1, cls.products_count + 1):
            product = Product.objects.create(
                name=f"Товар {i}",
                article=f"{i}",
                category=cls.category,
                price=i * 1000
            )
            shop.products.add(product)

            shop_product = ShopProduct.objects.get(product=product)
            shop_product.price_in_shop = i * 1000

            if i % 2 == 0:
                product.promotion_group = cls.promo_group
                product.rating = 100
            else:
                shop_product.promotion = cls.promo10

            product.save()
            shop_product.save()

    def test_index(self):
        """
        Проверка, что главная страница существует и использует правильный шаблон.
        """
        response = self.client.get(reverse("index"))

        self.assertEquals(response.status_code, 200)
        self.assertIn(Index.template_name, response.template_name)

    def test_show_popular_products(self):
        """
        Проверка, сколько товаров показывается в секции `Популярные товары`.
        """
        response = self.client.get(reverse("index"))

        self.assertEquals(response.status_code, 200)
        self.assertEquals(
            response.context_data["products"].count(),
            ShopProduct.objects.filter(product__rating__gte=100).count()
        )

    def test_show_discount_products(self):
        """
        Проверка, сколько товаров показывается в секции `Товары со скидкой`.
        """
        response = self.client.get(reverse("index"))

        self.assertEquals(response.status_code, 200)
        self.assertEquals(
            response.context_data["discounts"].count(),
            ShopProduct.objects.filter(~models.Q(promotion__isnull=True)).count()
        )
