from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import ProductCateogry, Product
from .serializers import ProductCateogrySerializer, ProductSerializer, SearchSerializer
from django.db.models import Q

# Product category create api
class ProductCateogryCreate(generics.ListCreateAPIView):

    queryset = ProductCateogry.objects.all()
    serializer_class = ProductCateogrySerializer

# Product Create api
class ProductCreate(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Search record api
class SearchAPIView(APIView):
  
    def get(self, request):
        query = request.GET.get('q')
        search_data = Product.objects.filter(Q(product_name__icontains=query)
                                | Q(color__icontains=query)
                                | Q(product_category__name_category__icontains=query))
        if search_data:
            serializer = SearchSerializer(instance=search_data, many=True)
            serialized_data = serializer.data
            return Response({
                'data': {
                    'content': serialized_data,
                },
                'success': 1
            }, status=status.HTTP_200_OK)

        else:
            response = {
                'status': False,
                'data': [],
                'message': "No Record found !!!"
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)


# # Create Product Category
# class ProductCateogryCreate(APIView):

#     def post(self, request):
#         data = request.data
#         product_category = data.get("product_category")
#         ProductCateogry.objects.create(
#             product_category = product_category,
#         )
#         return Response({
#             'success': 1,
#             'message': 'Product Category Created Successfully',
#         }, status=status.HTTP_200_OK)

# class ProductCreate(APIView):

#     def post(self, request):
#         data = request.data
#         product_category = data.get("product_category")
#         product_image = request.FILES.get('product_image')
#         product_name = data.get("product_name")
#         price = data.get("price")
#         color = data.get("color")
#         Product.objects.create(
#             product_category_id = product_category,
#             product_image = product_image,
#             product_name = product_name,
#             price = price,
#             color = color
#         )
#         return Response({
#             'success': 1,
#             'message': 'Product Created Successfully',
#         }, status=status.HTTP_200_OK)
