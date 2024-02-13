from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Cart, CartItem
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Tovar
from Main.models import SetMkMaterial
from .cart import Cart
from .forms import CartAddProductForm, CartAddTovarForm


@require_POST
def cart_add(request, tovar_id):
    cart = Cart(request)
    tovar = get_object_or_404(Tovar, id=tovar_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(tovar=tovar,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('catalog')


def card_add_all(request, tovar_id):
    cart = Cart(request)
    tovar = get_object_or_404(Tovar, id=tovar_id)
    settov = SetMkMaterial.objects.filter(MK=tovar)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(tovar=tovar,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    for el in settov:
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(tovar=el.Tovar,
                     quantity=cd['quantity'],
                     update_quantity=cd['update'])
    return redirect('catalog')


def cart_plus(request, tovar_id):
    cart = Cart(request)
    tovar = get_object_or_404(Tovar, id=tovar_id)
    form = CartAddTovarForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.quantity_tovar_plus(tovar=tovar, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_minus(request, tovar_id):
    cart = Cart(request)
    tovar = get_object_or_404(Tovar, id=tovar_id)
    form = CartAddTovarForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.quantity_tovar_minus(tovar=tovar, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, tovar_id):
    cart = Cart(request)
    tovar = get_object_or_404(Tovar, id=tovar_id)
    cart.remove(tovar)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})

    return render(request, 'cart/detail.html', {'cart': cart})


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return render(request, 'cart/detail.html')


# Create your views here.
