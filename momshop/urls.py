from django.contrib import admin
from django.conf.urls import url, include
from .views import (IndexView, CatalogView, category_view,
                    search, product_detail, about_us,
                    faq)
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^catalog/$', CatalogView.as_view(), name='catalog'),
    url(r'^catalog/cateregory_(?P<id>\d+)$', category_view, name='category-view'),
    url(r'^catalog/search/$', search, name='search'),
    url(r'^catalog/products/(?P<id>\d+)$', product_detail, name='product-detail'),
    url(r'^about_us$', about_us, name='about_us'),
    url(r'^faq/$', faq, name='faq'),
]
