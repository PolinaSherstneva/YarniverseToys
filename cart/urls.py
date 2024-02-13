from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:tovar_id>/',
         views.cart_add,
         name='cart_add'),
    path('addp/<int:tovar_id>/', views.cart_plus, name='cart_plus'),
    path('addm/<int:tovar_id>/', views.cart_minus, name='cart_minus'),
    path('addall/<int:tovar_id>/', views.card_add_all, name='card_add_all'),
    path('remove/<int:tovar_id>/',

         views.cart_remove,
         name='cart_remove'),
    path('clear/', views.cart_clear, name='cart_clear'),
]
