from django.conf import settings
from decimal import Decimal
from django.shortcuts import get_object_or_404
from services.models import Service


def cart_contents(request):

    cart_items = []
    total = 0
    service_count = 0

    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        service = get_object_or_404(Service, pk=item_id)
        total += quantity * service.price
        service_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'service': service,
        })

    if total < settings.DELIVERY_THRESHOLD:
        delivery = (total + settings.DELIVERY_CHARGE) * Decimal(settings.DELIVERY_PERCENT / 100)
        delivery_dearth = settings.DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        delivery_dearth = 0
    
    grand_total = delivery + total
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'service_count': service_count,
        'delivery': delivery,
        'delivery_dearth': delivery_dearth,
        'delivery_threshold': settings.DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context