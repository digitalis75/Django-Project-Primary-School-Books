from django.shortcuts import get_object_or_404
from products.models import Product


# Ensures that the cart contents are available when rendering every page
def cart_contents(request):
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 0

    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        product_total = quantity * product.price
        total += product_total
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product,
                                     'product_total': product_total})

    return {'cart_items': cart_items,
            'total': total,
            'product_count': product_count}
