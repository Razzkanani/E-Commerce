from django.urls import path, include
from .views import CustomersListCreateAPIView, CustomerUpdateAPIView


urlpatterns = [
    path('api/customers/', CustomersListCreateAPIView.as_view(), name='customer-list-create'),
    path('api/customers/<int:pk>/', CustomerUpdateAPIView.as_view(), name='customer-update'),
]