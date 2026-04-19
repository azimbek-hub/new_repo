from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Category, Product, Order,Cart
from .serializers import CategorySerializer, ProductSerializer,CartSerializer

class CartApiView(APIView):
    def get(self,request,format=None):
        categories = Cart.objects.all()
        serializer = CartSerializer(categories, many=True)
        return Response(serializer.data)