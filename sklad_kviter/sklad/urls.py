from django.urls import path

from .views import Sklad_list


urlpatterns = [
    path('', Sklad_list.as_view(), name='sklad_list_url'),
]