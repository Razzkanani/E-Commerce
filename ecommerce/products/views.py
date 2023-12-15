from .models import Product
from .serializers import ProductSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

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
            "message": "Your product created.",
            "data": response.data
        }
        return Response(data)