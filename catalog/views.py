from django.shortcuts import render
from catalog.models import Product

# Create your views here.

#def index(request):
 #   return render(request, 'catalog/index.html' )

def home(request):
    product_list = Product.objects.all()
    context = {'object_list': product_list, 'title': 'Перечень товаров'}

    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name  = request.POST.get('name')
        email = request.POST.get ('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({email}, {phone}): {message}')
    return render(request, 'catalog/contacts.html')

def products(request, pk):
    #product_item = Product.objects.get(pk=id)
    context = {'object_list': Product.objects.filter(pk=pk), 'title': 'Описание товара'}
    return render(request, 'catalog/products.html', context)