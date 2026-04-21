from django.db import models


class Item(models.Model):
    CURRENCY_CHOICES = [
        ('usd', 'USD'),
        ('eur', 'EUR'),
    ]

    name = models.CharField(max_length=250, verbose_name='Имя')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Цена')
    currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CHOICES,
        default='usd',
        verbose_name='Валюта'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Order(models.Model):
    items = models.ManyToManyField(Item, related_name='orders')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_total(self):
        # Общая стоимость товаров в заказе
        total = sum(item.price for item in self.items.all())
        self.total_price = total
        self.save()
        return total

    def get_currency(self):
        # Валюта для первого товара
        first_item = self.items.first()
        return first_item.currency if first_item else 'usd'

    def __str__(self):
        return f'Order #{self.id} - {self.total_price} {self.get_currency().upper()}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'