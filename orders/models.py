from django.db import models
from Main.models import Tovar
from users.models import CustomUser

Work = 'Принят в работу'
Sbor = 'В сборке'
Dost = 'В доставке'
Done = 'Выполнен'

CHOISE_STATUS = (
    (Work, "Принят в работу"),
    (Sbor, "В сборке"),
    (Dost, "В доставке"),
    (Done, "Выполнен"),
)


class Order(models.Model):
    user = models.ForeignKey(CustomUser, related_name='color_tovar', on_delete=models.CASCADE)
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица', null=True, blank=True)
    house = models.CharField(max_length=100, verbose_name='Дом')
    apartment = models.CharField(max_length=100, verbose_name='Квартира')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=CHOISE_STATUS, default=Work)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderTovar(models.Model):
    order = models.ForeignKey(Order, related_name='tovars', on_delete=models.CASCADE)
    tovar = models.ForeignKey(Tovar, related_name='tovar_in_order', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity



