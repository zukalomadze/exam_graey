from decimal import Decimal

from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Ticket(models.Model):
    name = models.CharField(verbose_name=_('Ticket Name'), max_length=255)
    start_date = models.DateTimeField(verbose_name=_('Start Time'))
    qrcode = models.CharField(verbose_name='qrcode', max_length=255, unique=True)


class Order(models.Model):
    Customer = models.ForeignKey(to='user.User', on_delete=models.SET_NULL, related_name='orders', null=True) # ar vici rato davwere didi asoti
    purchase_date = models.DateTimeField(auto_now=True, verbose_name="Purchase Date")
    Ticket = models.OneToOneField(to='ticketshop.Ticket', on_delete=models.SET_NULL, related_name='orders', null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=_('Price'), help_text='in Lari', default=Decimal(2))