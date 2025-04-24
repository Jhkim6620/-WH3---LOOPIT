from django.urls import path
from .views import ProductListCreateView, ProductDetailView, MyProductListView

urlpatterns = [
    path('products/', ProductListCreateView.as_view()),
    path('products/<int:pk>/', ProductDetailView.as_view()),
    path('myproduct/', MyProductListView.as_view(), name='my-product-list')
]
