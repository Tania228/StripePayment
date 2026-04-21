from django.contrib import admin
from .models import Item, Order


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'currency')
    list_filter = ('currency',)
    search_fields = ('name',)
    list_editable = ('price', 'currency')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_price', 'get_currency', 'created_at')
    list_filter = ('created_at',)
    filter_horizontal = ('items',)
    readonly_fields = ('total_price', 'created_at')

    def get_currency(self, obj):
        return obj.get_currency().upper()

    get_currency.short_description = 'Валюта'