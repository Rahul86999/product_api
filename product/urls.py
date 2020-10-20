
from django.urls import path
from .import views

urlpatterns = [
    path('create/category', views.ProductCateogryCreate.as_view(),name='create_category'),
    path('create', views.ProductCreate.as_view(),name='create_product'),
    path('search/', views.SearchAPIView.as_view(),name='search'),
] 