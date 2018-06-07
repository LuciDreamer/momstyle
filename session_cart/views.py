from django.shortcuts import render
from django.views.generic import TemplateView
from session_cart.cart import Cart
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
import json
from momshop.models import Products, Order, OrderItem
from decimal import Decimal


class CartView(TemplateView):

    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        cart = Cart(self.request)
        cart_items = cart.items_list
        total_price = cart.total_price
        context = {
            'cart_items': cart_items,
            'total_price': total_price,
            'cart': cart.items_count()
        }
        return context


@csrf_exempt
def add_item(request):

    print("add item view function started")
    cart = Cart(request)
    if request.method == 'POST' and request.is_ajax():
        product_id = request.POST['product_id']
        quantity = request.POST['quantity']
        size = request.POST['size']
        cart.add_item(request, product_id, quantity, size)
        items = cart.items_count()
    return  HttpResponse(json.dumps({'cart': items}))


@csrf_exempt
def set_quantity(request):
    cart = Cart(request)
    if request.method == 'POST' and request.is_ajax():
        product_id = request.POST['product-id']
        size = request.POST['size']
        action = request.POST['action']
        if action:
            cart.set_quantity(product_id, action, size)
            total_price = str(cart.total_price)
            response_dict = json.dumps({'total_price': total_price})
            return HttpResponse(response_dict)
    else:
        return Http404


def clean_cart(request):
    cart = Cart(request)
    cart.clean_cart()
    return HttpResponse('')


@csrf_exempt
def delete_item(request):
    cart = Cart(request)

    if request.method == 'POST' and request.is_ajax():
        product_id = request.POST['product_id']
        size = request.POST['size']
        cart.delete_item(product_id, size)
        total_price = str(cart.total_price)
        return_object = {
        }
        return HttpResponse(json.dumps({'total_price': total_price}))
    else:
        return Http404


@csrf_exempt
def order(request):
    cart = Cart(request)

    if request.method == 'POST' and request.is_ajax():
        name = request.POST['name']
        phone = request.POST['phone']
        order = Order(name=name,
                      phone_number=phone,
                      total=Decimal(cart.total_price))
        order.save()
        for item in cart.items_list:
            item_id = item['product_id']
            item_quantity = item['quantity']
            item = Products.objects.get(id=item_id)
            order_item = OrderItem(product=item, quantity=item_quantity, order=order)
            order_item.save()

        cart.clean_cart()

        return HttpResponse('')
    else:
        return Http404




