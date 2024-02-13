from django.urls import path
from . import views


app_name = 'orders'

urlpatterns = [
    path('createorder/', views.order_create, name='order_create'),
    path('myorders/', views.get_orders, name='get_orders'),
    path('adminorders/', views.get_admin_orders, name='get_admin_orders'),
    path('orderdetail/<int:order_id>', views.get_tovar_in_orders, name='get_tovar_in_orders'),
    path('ordercreated/', views.order_created, name='order_created'),
    path('MK/', views.get_mks, name='get_mks'),
    path('MK/<int:mk_id>', views.get_video_mk, name='get_video_mk'),

]


