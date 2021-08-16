from rest_framework import serializers

from quota.models import ExchangeRate


class ExchangeRateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExchangeRate
        fields = ('id', 'from_currency', 'to_currency', 'rate', 'bid_price', 'ask_price', 'created', 'modified', )
