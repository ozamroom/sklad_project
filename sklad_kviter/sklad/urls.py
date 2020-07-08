from django.urls import path

from .views import Sklad_list, Product_create, Update_roduct


urlpatterns = [
    path('', Sklad_list.as_view(), name='sklad_list_url'),
    path('product_create/', Product_create.as_view(), name='product_create_url'),
    path('<str:slug>/', Update_roduct.as_view(), name='update_product_url'),
]