from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter
from .viewsets import EquipViewSet

router = DefaultRouter()

router.register('equip', EquipViewSet)


urlpatterns = [
    url(r'', include(router.urls))
]
