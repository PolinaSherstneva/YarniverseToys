
from django.urls import path
from . import views
from users import views as user_views


urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('lk', views.lk, name="lk"),
    path('catalog', views.catalog, name="catalog"),
    path('create', views.create, name="create"),
    path('get_admin_feedback', views.get_admin_feedback, name="get_admin_feedback"),
    path('Tovar/<int:tovar_id>', views.get_set, name='tovar-detail'),
    path('Sub', views.sub, name="sub"),
    path('paysub', views.pay_sub, name="pay_sub"),
    path('sub_buy/<int:sub_id>', views.buy_sub, name="buy_sub"),
    path('about_app', views.about_app, name="about_app"),
    # path('Tovar/<int:tovar_id>', views.TovarDetailView.add, name='tovar-detail'),
    path('<int:tovar_id>/materials', views.get_set, name='mk-materials'),
    path('<int:pk>/update', views.TovarUpdateView.as_view(), name='tovar-update'),
    path('<int:pk>/delete', views.TovarDeleteView.as_view(), name='tovar-delete'),
]
