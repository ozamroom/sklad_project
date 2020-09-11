from django.urls import path

from .views import Sklad_list, Product_create, Product_update, Calculation


urlpatterns = [
    path('', Sklad_list.as_view(), name='sklad_list_url'),
    path('product_create/', Product_create.as_view(), name='product_create_url'),
    path('product/<str:slug>/', Product_update.as_view(), name='product_update_url'),
    path('calculation/', Calculation.as_view(), name='calculation_url'),
]