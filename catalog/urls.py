from django.urls import path
from django.views.decorators.cache import never_cache, cache_page

from catalog.apps import CatalogConfig
from catalog.views import contacts, index, CatalogListView, ProductCreateView, ProductListView, \
    ProductUpdateView, ProductDeleteView, ProductDetailView

app_name = CatalogConfig.name



urlpatterns = [
    path('contacts/', contacts),
    path('', index, name='index'),
    path('products/', ProductListView.as_view(), name='products'),
    path('catalog/<int:pk>/', CatalogListView.as_view(), name='inform'),
    path('<int:pk>/view_product/', cache_page(60)(ProductDetailView.as_view()), name='view_product'),
    path('create_product/', never_cache(ProductCreateView.as_view()), name='create_product'),
    path('<int:pk>/edit_product/', ProductUpdateView.as_view(), name='edit_product'),
    path('<int:pk>/product/', ProductDeleteView.as_view(), name='delete_product'),
]