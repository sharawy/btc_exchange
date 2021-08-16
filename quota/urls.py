from django.urls import include, path
from rest_framework.routers import DefaultRouter

from quota import views

router = DefaultRouter()
router.register(r'', views.QuotaViewSet, basename='quota_viewset')

urlpatterns = [
    path('', include(router.urls))
]
