from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from quota.exceptions import APIIntegrationException
from quota.models import ExchangeRate
from quota.serializers import ExchangeRateSerializer
from quota import tasks


class QuotaViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin, viewsets.GenericViewSet):

    queryset = ExchangeRate.objects.all().order_by('-created')
    serializer_class = ExchangeRateSerializer

    def create(self, request):
        try:
            tasks.fetch_last_quota_task()
        except APIIntegrationException as e:
            return Response(data={"error": e.message}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        return super().list(request)
