from rest_framework.views import APIView
from rest_framework.response import Response
 
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
 
class CategoryAPIView(APIView):
 
    def get(self, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
class ProductAPIView(APIView):

    def get(self, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, manu=True)
        return Response(serializer.data)