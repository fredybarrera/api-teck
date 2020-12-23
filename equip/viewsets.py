from django.db import connection
from django.db.models.aggregates import Max
from .models import Equip, EquipCoordTrans, MineOreQuality
from .serializers import EquipSerializer, EquipCoordTransSerializer, MineOreQualitySerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
import numpy
from decimal import Decimal
from decouple import config
import traceback


posiciones = []
data = []

class EquipViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating Equip."""

    serializer_class = EquipSerializer
    queryset = Equip.objects.all().order_by('-equip_ident')
    http_method_names = ['get']
    # queryset = Equip.objects.all()[0:1]

    def list(self, request):
        queryset = Equip.objects.all().values()
        serializer = EquipSerializer(queryset, many=True)
        posiciones = []
        data = []
        for index, item in enumerate(queryset):
            pos = getCoords(item)
            if pos:
                 posiciones.append(pos)
       
        data.append({'posiciones': posiciones})

        return Response({'Flota': data})


    @action(
        methods=['get'],
        detail=False,
        url_path='quality',
        url_name='quality',
    )
    def get_quality_equip(self, request, *args, **kwargs):
        # last_pk = self.queryset.all().last().pk
        # self.kwargs.update(pk=last_pk)
        # return self.retrieve(request, *args, **kwargs)
        with connection.cursor() as cursor:
            database = config('APP_DATABASE_NAME', default='')
            query = """
            SELECT t1.*
            FROM {0}.dbo.WENCO_MINE_ORE_QUALITY t1
            WHERE t1.DUMP_TIMESTAMP = (
                SELECT MAX(DUMP_TIMESTAMP) FROM teck.dbo.WENCO_MINE_ORE_QUALITY t2 
                where t1.HAULER_EQUIP_IDENT=t2.HAULER_EQUIP_IDENT);
            """.format(database)
            cursor.execute(query)
            row = cursor.fetchall()

        return Response({'data': row})


    @action(
        methods=['get'],
        detail=False,
        url_path='quality_v2',
        url_name='quality_v2',
    )
    def get_quality_equip_v2(self, request, *args, **kwargs):
        equips = MineOreQuality.objects.values(
            'hauler_equip_ident').annotate(dump_timestamp=Max('dump_timestamp')).values('dump_timestamp', 'hauler_equip_ident')
        row = []
        for equip in equips:
            result = MineOreQuality.objects.all().filter(
                hauler_equip_ident=equip['hauler_equip_ident'], dump_timestamp=equip['dump_timestamp']).values()
            row.append(result)

        return Response({'data': row})
    # http://127.0.0.1:8000/api/equip/quality_v2/?format=json


    @action(
        methods=['get'],
        detail=False,
        url_path='quality_v3',
        url_name='quality_v3',
    )
    def get_quality_equip_v3(self, request, *args, **kwargs):
        with connection.cursor() as cursor:
            database = config('APP_DATABASE_NAME', default='')
            query = """
            SELECT t1.*
            FROM [WencoCDA].[dbo].[HAUL_CYCLE_TRANS] t1
            WHERE t1.DUMP_END_TIMESTAMP = (
            SELECT MAX(DUMP_END_TIMESTAMP) FROM [WencoCDA].[dbo].[HAUL_CYCLE_TRANS] t2
            where t1.HAULING_UNIT_IDENT=t2.HAULING_UNIT_IDENT);
            """.format(database)
            cursor.execute(query)
            row = cursor.fetchall()

        return Response({'data': row})
    # http://127.0.0.1:8000/api/equip/quality_v3/?format=json


    @action(
        methods=['get'],
        detail=False,
        url_path='quality-count',
        url_name='quality-count',
    )
    def get_quality_equip_count(self, request, *args, **kwargs):
        count = MineOreQuality.objects.all().count()
        return Response({'data': count})


    @action(
        methods=['get'],
        detail=False,
        url_path='quality-last',
        url_name='quality-last',
    )
    def get_quality_equip_last(self, request, *args, **kwargs):
        last_pk = self.queryset.all().last().pk
        self.kwargs.update(pk=last_pk)
        return self.retrieve(request, *args, **kwargs)
        

def getCoords(item):

    with connection.cursor() as cursor:
        database = config('APP_DATABASE_NAME', default='')
        query = """
        select [TIMESTAMP],
        EQUIP_IDENT,
        SHIFT_DATE,
        SHIFT_IDENT,
        EASTING,
        NORTHING,
        ELEVATION,
        SPEED
        from {0}.dbo.EQUIP_COORD_TRANS 
        where EQUIP_IDENT = '{1}'
        order by [TIMESTAMP] desc
        OFFSET 0 ROWS
        FETCH NEXT 1 ROWS ONLY;
        """.format(database, item['equip_ident'])

        cursor.execute(query)
        row = cursor.fetchone()
        if row is not None:
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
            return aux
        
        return None








        

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def transform(EASTING, NORTHING, ELEVATION):

    X_PSAD56 = EASTING + 200000  # K4
    Y_PSAD56 = NORTHING + 6600000  # K5
    Z_PSAD56 = ELEVATION # K6
   
    resta_x = 182.81409164
    resta_y = 375.74430404

    X_WGS84 = X_PSAD56 - Decimal(resta_x)
    Y_WGS84 = Y_PSAD56 - Decimal(resta_y)
    Z_WGS84 = Z_PSAD56

    return [X_WGS84, Y_WGS84, Z_WGS84]
