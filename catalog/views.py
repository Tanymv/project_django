from django.shortcuts import render
from django.views.generic import ListView, CreateView

from catalog.models import Product


# Create your views here.

def contacts(request):
    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name')
        telephone = request.POST.get('phone')
        message = request.POST.get('message')
        # а также передается информация, которую заполнил пользователь
        print(name, telephone, message)
    return render(request, 'catalog/contacts.html')


def index(request):
    context = {
        'object_list': Product.objects.all(),
        'title': f"Магазин продуктов"
    }
    return render(request, 'catalog/index.html', context)

# def products(request):
#     context = {
#         'object_list': Product.objects.all(),
#         'title': f"Магазин продуктов"
#     }
#     return render(request, 'catalog/product_list.html', context)

class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': f"Магазин продуктов"
    }

# def inform(request, pk):
#     products_item = Product.objects.get(pk=pk)
#     context = {
#         'object_list': Product.objects.filter(pk=pk),
#         'title': f"{products_item.name}"
#     }
#     return render(request, 'catalog/catalog.html', context)

class CatalogListView(ListView):
    model = Product
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        products_item = Product.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = f"{products_item.title}"
        return context_data


