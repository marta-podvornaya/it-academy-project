from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name='index'),
    path("shopping-cart/", views.shopping_cart, name='cart'),
    path('checkout/', views.checkout),
    path('update_item/', views.updateItem, name='update_item'),
    path('registration/', views.registry, name='registry'),
    path('accounts/profile/', views.profile, name='profile'),
    path('catalog/<int:code>', views.item, name='item'),
    path('catalog/<str:code>', views.item, name='item'),
    path('form-success/', views.success_form, name='success'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls'))
]