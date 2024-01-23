from django.shortcuts import render

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

def categories(request):
    context = {
        'object_list': Product.objects.all(),
        'title': f"Магазин продуктов"
    }
    return render(request, 'catalog/categories.html', context)

def inform(request, pk):
    category_item = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f"{category_item.name}"
    }
    return render(request, 'catalog/catalog.html', context)