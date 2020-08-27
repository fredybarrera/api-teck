from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter
from .viewsets import EquipViewSet, EquipCoordTransViewSet

router = DefaultRouter()

router.register('equip', EquipViewSet)
# router.register('equip-coords-trans', EquipCoordTransViewSet)


urlpatterns = [
    url(r'', include(router.urls))
]
