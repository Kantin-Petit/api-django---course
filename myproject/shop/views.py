from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
 
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
 
class CategoryViewset(ModelViewSet):
 
    serialize_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()
    
class ProductViewset(ModelViewSet):

    serialize_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()
    