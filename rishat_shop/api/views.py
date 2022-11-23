import stripe
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from items.models import Item, Order

from rishat_shop.settings import STRIPE_PUBLISHABLE_KEY, STRIPE_SECRET_KEY

stripe.api_key = STRIPE_SECRET_KEY


def create_item_checkout_session(request, pk):
    """
    Creates a Stripe validation session and returns the ID for Item.
    """
    item = get_object_or_404(Item, pk=pk)
    try:
        session = stripe.checkout.Session.create(
            line_items=[{'price_data': {'currency': item.сurrency,
                                        'product_data': {'name': item.name, },
                                        'unit_amount': int(item.price * 100),
                                        },
                         'quantity': 1, }],
            mode='payment',
            success_url='http://localhost:4242/success',
            cancel_url='http://localhost:4242/cancel',)
        return JsonResponse({"id_session": session.get('id')}, status=200)
    except TypeError as e:
        return JsonResponse({str(e)}, status=403)


def payment_item_page(request, pk):
    """
    Item purchase page.
    """
    item = get_object_or_404(Item, pk=pk)
    return render(request, "checkout.html",
                           {"item": item,
                            "PUBLISHABLE_KEY": STRIPE_PUBLISHABLE_KEY})


def create_order_checkout_session(request, pk):
    """
    Creates a Stripe validation session and returns the ID for Order.
    """
    order = get_object_or_404(Order, pk=pk)
    list_item = [{"price_data": {"currency": сurrency,
                                 "product_data": {"name": name},
                                 "unit_amount": int(price * 100), },
                  "quantity": 1,
                  'tax_rates': [tax_rate]}
                 for name,
                 сurrency,
                 price,
                 tax_rate in order.items.values_list("name",
                                                     "сurrency",
                                                     "price",
                                                     "tax__tax_rate")]
    discount_list = [{'coupon': id, }
                     for id in order.discounts.values_list("name", flat=True)]

    try:
        session = stripe.checkout.Session.create(
            line_items=list_item,
            discounts=discount_list,
            mode='payment',
            success_url='http://localhost:4242/success',
            cancel_url='http://localhost:4242/cancel',)
        return JsonResponse({"id_session": session.get('id')}, status=200)
    except Exception as e:
        return JsonResponse(str(e), status=403)


def payment_order_page(request, pk):
    """
    Order purchase page.
    """
    order = get_object_or_404(Order, pk=pk)
    full_price = order.items.aggregate(Sum("price"))
    return render(request, "order.html",
                           {"order": order,
                            "full_price": full_price.get("price__sum"),
                            "PUBLISHABLE_KEY": STRIPE_PUBLISHABLE_KEY})
