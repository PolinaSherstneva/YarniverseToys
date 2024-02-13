from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tovar, Category, SetMkMaterial, Feedback, Subsc, SubType
from users.models import CustomUser
from .forms import TovarForm, FeedbackForm, SubForm
from django.views.generic import DetailView, UpdateView, DeleteView
from cart.forms import CartAddProductForm
from django.contrib.messages.views import messages
from cart.cart import Cart
from orders.models import OrderTovar, Order


@login_required
def product_detail(request, tovar_id):
    tovar = get_object_or_404(Tovar, id=tovar_id)

    if request.method == "POST":
        messages.success(request, f"{tovar.name_tovar} added to your cart.")
        return redirect("cart:add_to_cart", tovar_id=tovar.id)

    context = {
        "tovar": tovar,
    }

    return render(request, "Tovar/DVTovar.html", context)


def lk(request):
    user_profile = None
    if request.user.is_authenticated:
        user_profile = CustomUser.objects.get(phone_number=request.user.phone_number)

    context = {'user_profile': user_profile}
    return render(request, 'Main/LK_Profile.html', context)


class TovarDetailView(DetailView):
    model = Tovar
    template_name = 'Main/DVTovar.html'
    cart_tovar_form = CartAddProductForm()
    context_object_name = 'tovar'

    def add(request, tovar_id):
        tovar = get_object_or_404(Tovar, id=tovar_id, available=True)
        cart_tovar_form = CartAddProductForm()
        return render(request, 'Main/DVTovar.html', {'tovar': tovar, 'cart_tovar_form': cart_tovar_form})


def get_set(request, tovar_id):
    tovars = Tovar.objects.all()
    tovar = get_object_or_404(Tovar, id=tovar_id, available=True)
    setmkmat = SetMkMaterial.objects.filter(MK=tovar)
    cart_tovar_form = CartAddProductForm()
    return render(request, 'Main/DVTovar.html', {'tovars': tovars,'tovar': tovar, 'setmkmat': setmkmat, 'cart_tovar_form': cart_tovar_form})


class TovarUpdateView(UpdateView):
    model = Tovar
    success_url = '/catalog'
    template_name = 'Main/Create.html'
    form_class = TovarForm


class TovarDeleteView(DetailView):
    model = Tovar
    success_url = '/catalog'
    template_name = 'Main/Tovar-delete.html'


def index(request):
    return render(request, 'Main/Index.html')


def about(request):
    error = ''
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')
        else:
            error = 'Форма была неверной'
    form = FeedbackForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'Main/About.html', data)


def get_admin_feedback(request):
    feedback = Feedback.objects.all()
    if request.user.is_authenticated:
        user_profile = CustomUser.objects.get(phone_number=request.user.phone_number)
    return render(request, 'Main/Admin_feedback.html', {'feedback': feedback, 'user_profile': user_profile})


def catalog(request):
    cart = Cart(request)

    tovars = Tovar.objects.all()
    cart_tovar_form = CartAddProductForm()
    user_profile = None
    if request.user.is_authenticated:
        user_profile = CustomUser.objects.get(phone_number=request.user.phone_number)
    orders = Order.objects.filter(user=user_profile)
    tovarmk = OrderTovar.objects.filter(order__user=user_profile)
    MK = tovarmk.filter(tovar__category_tovar__name_category="Мастер-класс")
    return render(request, 'Main/Catalog.html', {'tovars': tovars,
                  'cart_tovar_form': cart_tovar_form, 'cart': cart, 'orders': orders, 'tovarmk': tovarmk, 'MK': MK})


def about_app(request):
    user_profile = None
    if request.user.is_authenticated:
        user_profile = CustomUser.objects.get(phone_number=request.user.phone_number)
    return render(request, 'Main/About_app.html', {'user_profile': user_profile})


def create(request):
    error = ''
    if request.method == "POST":
        form = TovarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = TovarForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'Main/Create.html', data)


def sub(request):
    user_profile = None
    if request.user.is_authenticated:
        user_profile = CustomUser.objects.get(phone_number=request.user.phone_number)
    sub = Subsc.objects.filter(user=request.user)
    subt = SubType.objects.all()

    return render(request, 'Main/Sub.html', {'subt': subt, 'sub': sub, 'user_profile': user_profile})


def pay_sub(request):
    return render(request, 'Main/PaySub.html')


def buy_sub(request, sub_id):
    sub = SubType.objects.get(id=sub_id)
    Subsc.objects.create(user=request.user, sub=sub)
    return redirect('pay_sub')


def product_detail(request, tovar_id):
    tovar = get_object_or_404(Tovar, id=tovar_id, available=True)
    cart_tovar_form = CartAddProductForm()
    return render(request, 'Main/detail.html', {'tovar': tovar,
                  'cart_tovar_form': cart_tovar_form})
