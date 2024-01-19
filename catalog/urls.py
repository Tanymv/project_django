from django.urls import path

from catalog.views import contacts, index

# app_name = 'catalog_list', 'home_list'

urlpatterns = [
    path('contacts/', contacts),
    path('', index),
]