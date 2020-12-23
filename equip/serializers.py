from rest_framework import serializers
from .models import Equip, EquipCoordTrans, MineOreQuality


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


class MineOreQualitySerializer(serializers.ModelSerializer):
    """Serializer del obtejo mineorequality."""

    class Meta:
        model = MineOreQuality
        fields = ('__all__')
