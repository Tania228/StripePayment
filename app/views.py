from django.http import JsonResponse, HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Item, Order
from django.conf import settings
import stripe


class BuyItemView(View):
    """
    Класс, с помощью которого можно получить id
    для оплаты выбранного товара

    GET /buy/{id}
    """

    def get(self, request: HttpRequest, id: int) -> HttpResponse:
        item = get_object_or_404(Item, pk=id)

        stripe.api_key = settings.STRIPE_SECRET_KEY

        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': item.currency,
                    'product_data': {'name': item.name},
                    'unit_amount': int(item.price * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/success/'),
            cancel_url=request.build_absolute_uri('/cancel/'),
        )

        return JsonResponse({'session_id': session.id})


class InfoItemView(View):
    """
    Класс, с помощью которого можно получить html-страницу
    с информацией о выбранном товаре

    GET /item/{id}
    """

    def get(self, request: HttpRequest, id: int) -> HttpResponse:
        item = get_object_or_404(Item, pk=id)
        context = {
            'item': item,
            'publishable_key': settings.PUBLISHABLE_KEY,
        }
        return render(request, 'item_info.html', context)


class SuccessView(View):
    """
     Класс, с помощью которого можно получить html-страницу
     об успешной оплате
    """

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'success.html')


class CancelView(View):
    """
     Класс, с помощью которого можно получить html-страницу
     об отмене оплаты
    """

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'cancel.html')


class BuyOrderView(View):
    """
    Класс, с помощью которого можно получить session_id
    для оплаты заказа с несколькими товарами

    GET /order/{order_id}
    """

    def get(self, request: HttpRequest, order_id: int) -> HttpResponse:
        order = get_object_or_404(Order, pk=order_id)

        total = order.calculate_total()

        first_item = order.items.first()
        currency = first_item.currency if first_item else 'usd'

        items_description = ", ".join([item.name for item in order.items.all()])

        stripe.api_key = settings.STRIPE_SECRET_KEY

        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': currency,
                    'product_data': {
                        'name': f'Заказ #{order.id}',
                        'description': items_description[:500],
                    },
                    'unit_amount': int(total * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/success/'),
            cancel_url=request.build_absolute_uri('/cancel/'),
        )

        return JsonResponse({'session_id': session.id})

