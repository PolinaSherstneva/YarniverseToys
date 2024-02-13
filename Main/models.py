from django.db import models
from users.models import CustomUser


class Feedback(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    email = models.EmailField(verbose_name='Почтовый адрес')
    message = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"


class Category(models.Model):
    name_category = models.CharField(max_length=50, verbose_name="Категория товара", db_index=True)

    def __str__(self):
        return self.name_category

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Color(models.Model):
    color = models.CharField(max_length=100, verbose_name="Цвет")
    img_color = models.ImageField(upload_to='', default='', blank=True)

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"
        ordering = ('color',)


class Tovar(models.Model):
    name_tovar = models.CharField(max_length=128, verbose_name="Название товара")
    category_tovar = models.ForeignKey(Category, related_name='tovars', on_delete=models.CASCADE, blank=True, default='')
    price_tovar = models.DecimalField(max_digits=10, verbose_name="Стоимость товара", decimal_places=2)
    img_tovar = models.ImageField(upload_to='', blank=True)
    url_tovar = models.URLField(max_length=300, blank=True)
    color = models.ForeignKey(Color, related_name='color_tovar', on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(verbose_name="Описание товара", blank=True)
    slug = models.CharField(max_length=150, db_index=True, unique=True)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ('name_tovar',)
        index_together = (('id', 'slug'),)


class SetMkMaterial(models.Model):
    name_set = models.CharField(max_length=50, verbose_name="Связка МК и материала", default='')
    MK = models.ForeignKey(Tovar, related_name='id_MK', on_delete=models.CASCADE)
    Tovar = models.ForeignKey(Tovar, related_name='id_tovar', on_delete=models.CASCADE)

    def __str__(self):
        return self.name_set

    class Meta:
        verbose_name = "Набор материалов"
        verbose_name_plural = "Наборы материалов"


class SubType(models.Model):
    name = models.CharField(max_length=50, verbose_name="Тип подписки")
    cost = models.CharField(max_length=50, verbose_name="Стоимость")
    period = models.CharField(max_length=50, verbose_name="Срок действия")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"


class Subsc(models.Model):
    user = models.ForeignKey(CustomUser, related_name="user", on_delete=models.CASCADE)
    sub = models.ForeignKey(SubType, related_name="sub", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Подписка клиента"
        verbose_name_plural = "Подписки клиентов"

