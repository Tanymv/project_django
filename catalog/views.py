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
    }
    return render(request, 'catalog/index.html', context)

