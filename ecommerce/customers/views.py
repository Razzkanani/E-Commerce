from rest_framework import generics
from rest_framework.response import Response
from .serializers import CustomerSerializer
from .models import Customer


class CustomersListCreateAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        data = {
            "status": response.status_code,
            "data": response.data,
        }
        return Response(data)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        data = {
            "status": response.status_code,
            "message": "Successfully customer created.",
            "data": response.data
        }
        return Response(data)


class CustomerUpdateAPIView(generics.UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def put(self, request, *args, **kwargs):
        response = self.partial_update(request, *args, **kwargs)
        data = {
            "status": response.status_code,
            "message": "Customer profile updated.",
            "data": response.data
        }
        return Response(data)