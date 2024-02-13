from decimal import Decimal
from django.conf import settings
from .models import Tovar


class Cart(object):

    def __init__(self, request):
        """
        Инициализация корзины
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # сохраняем ПУСТУЮ корзину в сессии
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
        Перебираем товары в корзине и получаем товары из базы данных.
        """
        tovar_ids = self.cart.keys()
        # получаем товары и добавляем их в корзину
        tovars = Tovar.objects.filter(id__in=tovar_ids)

        cart = self.cart.copy()
        for tovar in tovars:
            cart[str(tovar.id)]['tovar'] = tovar

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Считаем сколько товаров в корзине
        """
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, tovar, quantity=1, update_quantity=False):
        """
        Добавляем товар в корзину или обновляем его количество.
        """
        tovar_id = str(tovar.id)
        if tovar_id not in self.cart:
            self.cart[tovar_id] = {'quantity': 0, 'price': str(tovar.price_tovar)}

        if update_quantity:
            self.cart[tovar_id]['quantity'] = quantity
        else:
            self.cart[tovar_id]['quantity'] += quantity
        self.save()

    def quantity_tovar_plus(self, tovar, quantity, update_quantity=False):
        tovar_id = str(tovar.id)
        self.cart[tovar_id]['quantity'] += 1
        self.save()

    def quantity_tovar_minus(self, tovar, quantity, update_quantity=False):
        tovar_id = str(tovar.id)
        if quantity != 1:
            self.cart[tovar_id]['quantity'] -= 1
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        # сохраняем товар
        self.session.modified = True

    def remove(self, tovar):
        """
        Удаляем товар
        """
        tovar_id = str(tovar.id)
        if tovar_id in self.cart:
            del self.cart[tovar_id]
            self.save()

    def get_total_price(self):
        # получаем общую стоимость
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # очищаем корзину в сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True


