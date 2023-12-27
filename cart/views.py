from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from flower.models import Product
from .cart import Cart
from .forms import CartAddProductForm

menu = [
    {'title': "О нас", 'url_name': 'about'},
    {'title': "Новости", 'url_name': 'news'},
    {'title': "Условия работы", 'url_name': 'working_conditions'},
    {'title': "Отзывы", 'url_name': 'reviews'},
    {'title': "Контакты", 'url_name': 'contacts'},
    {'title': "Статьи", 'url_name': 'articles'}
]


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart, 'menu': menu})