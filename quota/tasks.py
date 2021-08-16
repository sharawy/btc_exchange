from celery import shared_task

from quota.models import ExchangeRate
from quota.utils import fetch_last_quota


@shared_task(bind=False)
def fetch_last_quota_task():
    fetch_last_quota(ExchangeRate.BTC, ExchangeRate.USD)
