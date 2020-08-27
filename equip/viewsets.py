from django.db import connection
from .models import Equip, EquipCoordTrans
from .serializers import EquipSerializer, EquipCoordTransSerializer
from rest_framework import viewsets
from rest_framework.response import Response
import numpy

posiciones = []
data = []

class EquipViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating Equip."""

    serializer_class = EquipSerializer
    queryset = Equip.objects.all().order_by('-equip_ident')
    # queryset = Equip.objects.all()[0:1]

    def list(self, request):
        queryset = Equip.objects.all().values()
        serializer = EquipSerializer(queryset, many=True)
        for index, item in enumerate(queryset):
            getCoords(item)
       
        # print('data: ', data)
        data.append({'posiciones': posiciones})

        return Response({'Flota': data})



class EquipCoordTransViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating EquipCoordTrans."""

    serializer_class = EquipCoordTransSerializer
    # queryset = EquipCoordTrans.objects.all().order_by('timestamp')
    queryset = EquipCoordTrans.objects.all()[0:100]


def getCoords(item):

    with connection.cursor() as cursor:
        query = """
        select [TIMESTAMP],
        EQUIP_IDENT,
        SHIFT_DATE,
        SHIFT_IDENT,
        EASTING,
        NORTHING,
        ELEVATION,
        SPEED
        from teck.dbo.EQUIP_COORD_TRANS 
        where EQUIP_IDENT = '{0}'
        order by [TIMESTAMP] desc
        OFFSET 0 ROWS
        FETCH NEXT 1 ROWS ONLY;
        """.format(item['equip_ident'])

        cursor.execute(query)
        row = cursor.fetchone()
        if row is not None:
            # print('item: ', item)
            # print('row: ', row)
            easting, northing, elevation = transform(row[4], row[5], row[6])
            aux = {
                'TIMESTAMP': row[0],
                'EQUIP_IDENT': row[1],
                'SHIFT_DATE': row[2],
                'SHIFT_IDENT': row[3],
                # 'EASTING_original': row[4],
                # 'NORTHING_original': row[5],
                # 'ELEVATION_original': row[6],
                'EASTING': easting,
                'NORTHING': northing,
                'ELEVATION': elevation,
                'SPEED': row[7],
                'NAME': item['name'],
                'DESCRIP': item['descrip'],
                'EQP_TYPE': item['eqp_type'],
                'FLEET_IDENT': item['fleet_ident']
            }
            posiciones.append(aux)


def transform(EASTING, NORTHING, ELEVATION):

    easting_aux = str(EASTING)
    northing_aux = str(NORTHING)
    elevation_aux = str(ELEVATION)

    easting = easting_aux.replace(".0000", "")
    northing = northing_aux.replace(".0000", "")
    elevation = elevation_aux.replace(".0000", "")
    
    int_easting = float(easting)
    int_northing = float(northing)
    int_elevation = float(elevation)

    X_PSAD56 = (int_easting/10000)+200000  # K4
    Y_PSAD56 = (int_northing/10000)+6600000  # K5
    Z_PSAD56 = int_elevation/10000  # K6

    resta_x = 182.81409164
    resta_y = 375.74430404

    X_WGS84 = X_PSAD56 - resta_x
    Y_WGS84 = Y_PSAD56 - resta_y
    Z_WGS84 = Z_PSAD56

    return [X_WGS84, Y_WGS84, Z_WGS84]
