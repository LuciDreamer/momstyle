from django.conf.urls import url
from .views import (CartView, add_item, clean_cart,
                    delete_item, set_quantity, order)

urlpatterns = [
    url(r'^$', CartView.as_view(), name='cart'),
    url(r'^add_item/$', add_item, name='add_item'),
    url(r'^set_quantity/$', set_quantity, name='set_quantity'),
    url(r'^clean/$', clean_cart, name='clean_cart'),
    url(r'^delete-item$', delete_item, name='delete_item'),
    url(r'^order/$', order, name='order'),
]
