from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, index, ProductListView, CatalogListView

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', contacts),
    path('', index, name='index'),
    path('products/', ProductListView.as_view(), name='products'),
    path('catalog/<int:pk>/', CatalogListView.as_view(), name='inform'),

]