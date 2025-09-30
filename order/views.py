from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import title

from .models import Order, OrderItem
from products.models import Product
from account.models import CustomUser
from django.contrib import messages



# Create your views here.
@login_required (login_url='login')
def cart(request):
    order = Order.objects.filter(user=request.user, order_status=Order.CART_STAGE).first()
    order_items = order.items.all()
    grand_total = sum(item.product.price * item.quantity for item in order_items)
    context = {
        "order": order,
        "order_items": order_items,
        "grand_total": grand_total,
    }
    return render(request, "cart.html", context)


def remove_from_cart(request, item_id):
    item = get_object_or_404(OrderItem, id=item_id, order__user=request.user, order__order_status=Order.CART_STAGE)
    item.delete()
    return redirect('cart/')


@login_required (login_url='login')
def add_to_cart(request):
    if request.method == "POST":
        customer = request.POST.get("username")
        product_id = request.POST.get("product_id")
        product = Product.objects.get(id = product_id)
        quantity = request.POST.get("quantity")
        cart_item , created = Order.objects.get_or_create(
            user = customer,
            order_status = Order.CART_STAGE
        )

        order_item, created = OrderItem.objects.get_or_create(
            order = cart_item,
            product = product,
            quantity = int(quantity)
        )

        if not created:
            order_item.quantity += 1
            order_item.save()
            messages.success(request, f"Updated {product.title} quantity in your cart.")
        else:
            messages.success(request, f"{product.title} added to your cart.")

    return redirect('cart/')

@login_required (login_url='login_page')
def checkout(request):
    return render(request, "checkout.html")
