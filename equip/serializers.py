from rest_framework import serializers
from .models import Equip, EquipCoordTrans


class EquipSerializer(serializers.ModelSerializer):
    """Serializer del obtejo equip."""

    class Meta:
        model = Equip
        fields = ('__all__')


class EquipCoordTransSerializer(serializers.ModelSerializer):
    """Serializer del objeto equipcoordtrans."""

    class Meta:
        model = EquipCoordTrans
        fields  = ('__all__')
