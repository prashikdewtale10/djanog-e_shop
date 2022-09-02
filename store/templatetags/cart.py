from django import template

#decorator
register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    keys=cart.keys()
    for id in  keys:
        if int(id)==product.id:
            return True
    return False

@register.filter(name='cart_count')
def cart_count(product,cart):
    keys=cart.keys()
    for id in  keys:
        if int(id)==product.id:
            return cart.get(id)
    return False

@register.filter(name='total_price')
def total_price(product,cart):
    return product.price*cart_count(product,cart)

@register.filter(name='product_total_price')
def product_total_price(products,cart):
    sum=0
    for p in products:
        sum+=total_price(p,cart)
    return sum