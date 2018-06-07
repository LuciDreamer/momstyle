from django.shortcuts import render
from django.views.generic import View, TemplateView, DetailView
from .models import (Category, Products, Carousel,
                     AboutUsGallery, AboutUsDesc, FAQ,
                     Reviews)
from session_cart.cart import Cart
from .forms import SearchForm
import random
import json

class IndexView(View):

    def get(self, request):
        search = SearchForm()
        categories_all = Category.objects.all()
        categories = Category.objects.all()[:4]
        new_products = Products.objects.filter(availability=True).order_by('-creation')[:6]
        carousel = Carousel.objects.first()
        carousel_no_first = Carousel.objects.exclude()[1:]
        cart = Cart(request)
        reviews = Reviews.objects.all()
        

        context = {
            'categories': categories,
            'categories_all': categories_all,
            'new_products': new_products,
            'search': search,
            'carousel': carousel,
            'carousel_no_first': carousel_no_first,
            'cart': cart.items_count(),
            'reviews': reviews,
        }
        return render(request, 'index.html', context)


class CatalogView(TemplateView):

    template_name = 'catalog.html'

    def get_context_data(self, **kwargs):

        categories = Category.objects.all()
        products = Products.objects.filter(availability=True)
        cart = Cart(self.request)

        context = {
            'categories': categories,
            'products': products,
            'cart': cart.items_count(),
        }
        return  context


def category_view(request, id):
    category = Category.objects.get(id=id)
    key_group = Products.objects.filter(availability=True).filter(category=category)
    categories = Category.objects.all()
    cart = Cart(request)

    context = {
        'categories': categories,
        'category': category,
        'cart': cart.items_count(),
        'key_group': key_group,
    }

    return render(request, 'category.html', context)


def search(request):
    cart = Cart(request)
    param = request.POST.get('search')
    categories = Category.objects.all()
    key_group = Products.objects.filter(availability=True).filter(tags__name__iexact=param)
    if len(key_group) == 0:
        key_group = Products.objects.filter(availability=True)

    context = {
        'key_group':key_group,
        'categories': categories,
        'cart': cart.items_count(),
        'param': param
    }
    return render(request, 'search.html', context)


def product_detail(request, id):

    product_id = id
    product = Products.objects.get(id=product_id)
    availability = product.avalability_type
    if availability == 'a':
        availability_type = 'в наличии'
    else:
        availability_type = 'под заказ'

    param = product.category
    suggestions = Products.objects.filter(category=param).exclude(id=product.id)
    cart = Cart(request)


    context = {
        'product': product,
        'suggestions': suggestions,
        'cart': cart.items_count(),
        'availability': availability_type,

    }
    return render(request, 'product-detail.html', context)

def about_us(request):
    cart = Cart(request)
    gallery = AboutUsGallery.objects.all()
    description = AboutUsDesc.objects.first()
    context = {
        'cart': cart.items_count(),
        'gallery': gallery,
        'description': description,
    }
    return render(request, 'about_us.html', context)

def faq(request):
    faq_questions = FAQ.objects.all()
    cart = Cart(request)
    cart_items_count = cart.items_count()
    context = {
        'faq': faq_questions,
        'cart': cart_items_count,
    }
    return render(request, 'faq.html', context)



