from django.urls import path
from shop.views import ShopCreateView, ShopListView
urlpatterns = [
    path('shops/', ShopListView.as_view(), name='shop-list'),
    path('create/', ShopCreateView.as_view(), name='create-shop'),

]
