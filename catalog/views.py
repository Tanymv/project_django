from django.shortcuts import render

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


def home(request):
    return render(request, 'catalog/home.html')
