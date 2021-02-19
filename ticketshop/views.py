from django.db.models import Sum
from django.shortcuts import render
from django.utils import timezone

from ticketshop.models import Order, Ticket
from user.models import User

# Create your views here.


def order_list(request):
    current_user = request.user
    length = request.GET.get('length')
    if length == 'week':
        orders = Order.objects.filter(Customer=current_user,
                                      purchase_date__gt=timezone.now() - timezone.timedelta(weeks=1))
    elif length == 'month':
        orders = Order.objects.filter(Customer=current_user,
                                      purchase_date__gt=timezone.now() - timezone.timedelta(days=30))
    elif length == 'year':
        orders = Order.objects.filter(Customer=current_user,
                                      purchase_date__gt=timezone.now() - timezone.timedelta(days=365))
    else:
        orders = Order.objects.filter(Customer=current_user)

    if len(orders):
        sum_prices = orders.aggregate(Sum('price'))['price__sum']
    else:
        sum_prices = 0
    return render(
        request,
        'tickets/order_list.html',
        context={
            'orders': orders,
            'length': length,
            'sum_prices': sum_prices,
        }
    )
