from django.db import models
from users.models import CustomUser
from Main.models import Tovar
from django.urls import reverse


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    item = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.item}"

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    tovar_id = models.ForeignKey(Tovar, related_name='tovars', on_delete=models.CASCADE, blank=True, default='')
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.tovar_id)

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзине"

