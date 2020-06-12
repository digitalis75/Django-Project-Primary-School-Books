from django.shortcuts import render, redirect, reverse


# Create your views here.
# Renders the cart contents page
def view_cart(request):
    return render(request, "cart.html")


# Add a quantity of the specified product to the cart
def add_to_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


# Adjust the quantity of the specified product to the specified amount
def adjust_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


# Delete cart item
def delete_cart_item(request, id):
    cart = request.session.get('cart', {})

    cart.pop(id)
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
