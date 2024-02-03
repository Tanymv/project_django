from django.conf import settings
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from pytils.translit import slugify

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


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
#     return render(request, 'catalog/category_list.html', context)





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


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')



class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': "Каталог продуктов",
        'current_user': settings.AUTH_USER_MODEL,
    }



class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        version_formset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = version_formset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = version_formset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)



class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products')





class ProductDetailView(DetailView):
    model = Product
    extra_context = {
        'title': "Карточка продукта",
    }


def published(request, pk):
    prod_item = get_object_or_404(Product, pk=pk)
    if prod_item.is_published:
        prod_item.is_published = False
    else:
        prod_item.is_published = True
    prod_item.save()
    return redirect(reverse('catalog:home'))
