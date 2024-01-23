from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, index, categories, inform

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', contacts),
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
    path('<int:pk>/catalog/', inform, name='inform'),
]