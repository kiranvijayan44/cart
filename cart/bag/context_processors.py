from . models import Bag, CartItem
from . views import _bag_id

def counter(request):
    item_count= 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Bag.objects.filter(bag_id=_bag_id(request))
            cart_items = CartItem.objects.all().filter(bag=cart[:1])
            for cart_item in cart_items:
                item_count += cart_item.quantity
        except Bag .DoesNotExist:
            item_count = 0
    return dict(item_count=item_count)

