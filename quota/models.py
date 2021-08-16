from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.models import TimeStampedModel


class ExchangeRate(TimeStampedModel):
    BTC = "BTC"
    USD = "USD"
    CURRENCIES_CHOICES = (
        (BTC, _('Bitcoin')),
        (USD, _('United States Dollar')),
    )
    from_currency = models.CharField(max_length=4, choices=CURRENCIES_CHOICES, default=BTC)
    to_currency = models.CharField(max_length=4, choices=CURRENCIES_CHOICES, default=USD)
    rate = models.DecimalField(decimal_places=9, max_digits=20)
    bid_price = models.DecimalField(decimal_places=9, max_digits=20)
    ask_price = models.DecimalField(decimal_places=9, max_digits=20)
