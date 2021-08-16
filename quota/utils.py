from quota.clients import CryptoProviderClient
from quota.models import ExchangeRate


def fetch_last_quota(from_currency, to_currency):
    client = CryptoProviderClient()
    data = client.get_exchange_rates(from_currency, to_currency)
    last_quota = data['Realtime Currency Exchange Rate']
    ExchangeRate.objects.create(from_currency=from_currency, to_currency=to_currency,
                                rate=last_quota['5. Exchange Rate'], bid_price=last_quota['8. Bid Price'],
                                ask_price=last_quota['9. Ask Price'])
