from django.urls import path
from .views import OrderListCreateAPIView, OrderUpdateAPIView


urlpatterns = [
    path('api/orders/', OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('api/orders/<int:pk>/', OrderUpdateAPIView.as_view(), name='order-update'),
]
