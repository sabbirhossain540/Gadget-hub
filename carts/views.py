from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from store.models import Product, Variation
from .models import Cart, CartItem
#from .models import Cart, CartItem


# Create your views here.


def _cart_id(request):
    cart = request.session.session_key

    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    product_variation = []
    
    if request.method == 'POST':
            for item in request.POST:
                key = item
                value = request.POST[key]

                try:
                    variation = Variation.objects.get(product=product, variation_category__iexact=key, variation_value__iexact=value)
                    product_variation.append(variation)
                except:
                    pass
    
    
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()
    

    if_cart_item_exists = CartItem.objects.filter(product=product, cart=cart).exists()
    if if_cart_item_exists:
        #return HttpResponse(cart)
        cart_item = CartItem.objects.filter(product=product, cart=cart)


        ## Work From Here  ( 12:10 )


        ex_var_list = []
        for item in cart_item:
            return HttpResponse(item.variations)
            existing_variation = item.variations.all()
            return HttpResponse(existing_variation)
            ex_var_list.append(['sss', 'ssss'])
            return HttpResponse(ex_var_list)

        if product_variation in ex_var_list:
            return HttpResponse('true')
        else:
            return HttpResponse('false')
        
        #cart_item = CartItem.objects.get(product=product, cart=cart)
        if len(product_variation) > 0:
            cart_item.variations.clear()
            for item in product_variation:
                cart_item.variations.add(item)

        #return HttpResponse(cart)
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart
        )
        if len(product_variation) > 0:
            cart_item.variations.clear()
            for item in product_variation:
                cart_item.variations.add(item)

        cart_item.save()

    return redirect('cart')

def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    
    return redirect('cart')


def remove_cart_item(request, product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart')



def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        
        cart_items = CartItem.objects.filter(cart=cart, is_activate=True)
        
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        
        tax = (2 * total)/100
        grand_total = total + tax

    except ObjectDoesNotExist:
        pass
    
    context = {
        'total' : total,
        'quantity' : quantity,
        'carts_items' : cart_items,
        'tax' : tax,
        'grand_total' : grand_total,
    }

    #return HttpResponse(context)
    
    return render(request, 'store/cart.html', context)
