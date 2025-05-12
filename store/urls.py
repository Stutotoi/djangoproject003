from django.urls import path
from .views import home
from .views import home, product_detail

urlpatterns = [
    path('', home, name='home'),
]

urlpatterns = [
    path('', home, name='home'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
]
