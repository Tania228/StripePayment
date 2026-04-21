from django.urls import path
from .views import BuyItemView, InfoItemView, SuccessView, CancelView, BuyOrderView

urlpatterns = [
    path('buy/<int:id>/', BuyItemView.as_view(), name='buy_item'),
    path('item/<int:id>/', InfoItemView.as_view(), name='info_item'),
    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('order/<int:order_id>/', BuyOrderView.as_view(), name='buy_order'),
]

