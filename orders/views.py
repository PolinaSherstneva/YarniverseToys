from django.shortcuts import render, redirect
from .models import OrderTovar, CustomUser, Order, Tovar
from .forms import OrderCreateForm, OrderChangeStatus
from cart.cart import Cart


def order_created(request):
    return render(request, 'orders/order/created.html')


def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart:
                OrderTovar.objects.create(order=order, tovar=item['tovar'], price=item['price'], quantity=item['quantity'])
                tov = Tovar.objects.get(slug=item['tovar'])
                if tov.category_tovar.name_category != 'Мастер-класс':
                    tov.stock -= item['quantity']
                    tov.save()
            cart.clear()
            return render(request, 'orders/order/PayOrd.html', {'order': order, 'tov': tov})
    else:
        form = OrderCreateForm
        return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})


def get_orders(request):

    user_profile = None
    if request.user.is_authenticated:
        user_profile = CustomUser.objects.get(phone_number=request.user.phone_number)
    orders = Order.objects.filter(user=user_profile)

    return render(request, 'orders/order/orders.html', {'orders': orders, 'user_profile': user_profile})


def get_admin_orders(request):
    orders = Order.objects.all()
    user_profile = None
    if request.user.is_authenticated:
        user_profile = CustomUser.objects.get(phone_number=request.user.phone_number)

    return render(request, 'orders/order/orders_admin.html', {'orders': orders, 'user_profile': user_profile})


def get_tovar_in_orders(request, order_id):
    order = Order.objects.get(id=order_id)
    tovar = OrderTovar.objects.filter(order=order)
    if request.user.is_authenticated:
        user_profile = CustomUser.objects.get(phone_number=request.user.phone_number)
    form = OrderChangeStatus(request.POST, instance=order)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return render(request, 'orders/order/order-detail.html',
                          {'order': order, 'tovar': tovar, 'user_profile': user_profile, 'form': form})
    return render(request, 'orders/order/order-detail.html',
                  {'order': order, 'tovar': tovar, 'user_profile': user_profile, 'form': form})


def get_mks(request):

    user_profile = None
    if request.user.is_authenticated:
        user_profile = CustomUser.objects.get(phone_number=request.user.phone_number)
    orders = Order.objects.filter(user=user_profile)
    tovars = OrderTovar.objects.filter(order__user=user_profile)
    MK = tovars.filter(tovar__category_tovar__name_category="Мастер-класс")
    return render(request, 'orders/order/MK.html', {'orders': orders, 'user_profile': user_profile, 'MK': MK, 'tovars': tovars})


def get_video_mk(request, mk_id):
    user_profile = None
    if request.user.is_authenticated:
        user_profile = CustomUser.objects.get(phone_number=request.user.phone_number)
    MasClas = Tovar.objects.get(id=mk_id)

    return render(request, 'orders/order/MK-detail.html',
                  {'MasClas': MasClas, 'user_profile': user_profile})
