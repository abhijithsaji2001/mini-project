from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path("product_list", views.product_list, name="product_list"),
    path("product_detail/<int:pk>", views.product_detail, name="product_detail"),
    path('search_product', views.search_product, name= 'search_product'),
    path('product_shoes', views.product_shoes, name = 'product_shoes'),
    path('product_dress', views.product_dress, name = 'product_dress'),
    path('product_cosmetics', views.product_cosmetics, name = 'product_cosmetics'),
    path('product_grocery', views.product_grocery, name = 'product_grocery'),
]
