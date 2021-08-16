import logging

import requests
from django.conf import settings

from quota.exceptions import APIIntegrationException

logger = logging.getLogger(__name__)


class CryptoProviderClient(object):

    def __init__(self):
        """
        Initialize client.

        :param host: hostname to connect to
        :type host: string
        :param verify_ssl: verify SSL certificates for HTTPS requests
        :type verify_ssl: bool

        """
        self._base_url = 'https://{0}/query'.format(settings.CRYPTO_PROVIDER_HOST)
        self._api_key = settings.CRYPTO_PROVIDER_API_KEY

    def get_exchange_rates(self, from_currency, to_currency):

        params = {
            "function": "CURRENCY_EXCHANGE_RATE",
            "from_currency": from_currency,
            "to_currency": to_currency,
            "apikey": self._api_key
        }

        response = requests.get(self._base_url, params=params)
        if response.status_code != requests.codes.ok:
            logger.error(
                'Got response from crypto provider: content: {} , status_code:{}'.format(response.content,
                                                                                         response.status_code))
            raise APIIntegrationException("Integration Error with crypto provider {}".format(response.content))
        else:
            logger.info(
                'Got response from provider: content: {} , status_code:{}'.format(response.content,
                                                                                  response.status_code))
            data = response.json()
            if "Error Message" in data:
                raise APIIntegrationException("Integration Error with crypto provider {}".format(response.content))

            return data
