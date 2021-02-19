from django.urls import path

from ticketshop.views import order_list

app_name = 'tickets'

urlpatterns = [
    path('', order_list, name='order_list')
]