# Generated by Django 2.1.15 on 2020-08-24 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equip',
            fields=[
                ('equip_ident', models.CharField(db_column='EQUIP_IDENT', max_length=6, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='NAME', max_length=24, null=True)),
                ('descrip', models.CharField(blank=True, db_column='DESCRIP', max_length=35, null=True)),
                ('eqp_type', models.CharField(blank=True, db_column='EQP_TYPE', max_length=3, null=True)),
                ('fleet_ident', models.CharField(blank=True, db_column='FLEET_IDENT', max_length=3, null=True)),
                ('chklist_ident', models.IntegerField(blank=True, db_column='CHKLIST_IDENT', null=True)),
                ('fuel_normal_hour', models.DecimalField(blank=True, db_column='FUEL_NORMAL_HOUR', decimal_places=1, max_digits=6, null=True)),
                ('fuel_fill_hour', models.DecimalField(blank=True, db_column='FUEL_FILL_HOUR', decimal_places=1, max_digits=6, null=True)),
                ('fuel_critical', models.DecimalField(blank=True, db_column='FUEL_CRITICAL', decimal_places=1, max_digits=6, null=True)),
                ('fuel_capacity', models.DecimalField(blank=True, db_column='FUEL_CAPACITY', decimal_places=1, max_digits=6, null=True)),
                ('gps_flag', models.CharField(blank=True, db_column='GPS_FLAG', max_length=1, null=True)),
                ('mdt_flag', models.CharField(blank=True, db_column='MDT_FLAG', max_length=1, null=True)),
                ('smu_flag', models.CharField(blank=True, db_column='SMU_FLAG', max_length=1, null=True)),
                ('serial_number', models.CharField(blank=True, db_column='SERIAL_NUMBER', max_length=40, null=True)),
                ('model_number', models.CharField(blank=True, db_column='MODEL_NUMBER', max_length=40, null=True)),
                ('manufacturer', models.CharField(blank=True, db_column='MANUFACTURER', max_length=15, null=True)),
                ('business_unit', models.DecimalField(blank=True, db_column='BUSINESS_UNIT', decimal_places=0, max_digits=6, null=True)),
                ('owner', models.CharField(blank=True, db_column='OWNER', max_length=20, null=True)),
                ('manufacturer_date', models.CharField(blank=True, db_column='MANUFACTURER_DATE', max_length=50, null=True)),
                ('wenco_entry_date', models.CharField(blank=True, db_column='WENCO_ENTRY_DATE', max_length=50, null=True)),
                ('cost_code', models.CharField(blank=True, db_column='COST_CODE', max_length=5, null=True)),
                ('workorder', models.CharField(blank=True, db_column='WORKORDER', max_length=8, null=True)),
                ('ani', models.DecimalField(blank=True, db_column='ANI', decimal_places=0, max_digits=5, null=True)),
                ('ip_address', models.CharField(blank=True, db_column='IP_ADDRESS', max_length=15, null=True)),
                ('ip_port', models.DecimalField(blank=True, db_column='IP_PORT', decimal_places=0, max_digits=6, null=True)),
                ('eqmodel_code', models.CharField(blank=True, db_column='EQMODEL_CODE', max_length=15, null=True)),
                ('hide_from_fleet_control', models.CharField(blank=True, db_column='HIDE_FROM_FLEET_CONTROL', max_length=1, null=True)),
                ('active', models.CharField(blank=True, db_column='ACTIVE', max_length=1, null=True)),
                ('test', models.CharField(blank=True, db_column='TEST', max_length=1, null=True)),
                ('device_name', models.CharField(blank=True, db_column='DEVICE_NAME', max_length=32, null=True)),
                ('os_version', models.CharField(blank=True, db_column='OS_VERSION', max_length=12, null=True)),
                ('mdt_version', models.CharField(blank=True, db_column='MDT_VERSION', max_length=12, null=True)),
                ('dmp_address', models.CharField(blank=True, db_column='DMP_ADDRESS', max_length=8, null=True)),
                ('channel', models.DecimalField(blank=True, db_column='CHANNEL', decimal_places=0, max_digits=2, null=True)),
                ('comment', models.CharField(blank=True, db_column='COMMENT', max_length=255, null=True)),
                ('mdt_text', models.CharField(blank=True, db_column='MDT_TEXT', max_length=35, null=True)),
                ('v2x_mac_address', models.CharField(blank=True, db_column='V2X_MAC_ADDRESS', max_length=17, null=True)),
                ('next_inspection_alert_smu_hours', models.FloatField(blank=True, db_column='NEXT_INSPECTION_ALERT_SMU_HOURS', null=True)),
                ('next_inspection_alert_traveled_distance', models.FloatField(blank=True, db_column='NEXT_INSPECTION_ALERT_TRAVELED_DISTANCE', null=True)),
            ],
            options={
                'db_table': 'EQUIP',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EquipCoordTrans',
            fields=[
                ('timestamp', models.CharField(db_column='TIMESTAMP', max_length=24, primary_key=True, serialize=False)),
                ('equip_ident', models.CharField(db_column='EQUIP_IDENT', max_length=6)),
                ('shift_date', models.CharField(blank=True, db_column='SHIFT_DATE', max_length=24, null=True)),
                ('shift_ident', models.CharField(blank=True, db_column='SHIFT_IDENT', max_length=1, null=True)),
                ('northing', models.DecimalField(blank=True, db_column='NORTHING', decimal_places=4, max_digits=15, null=True)),
                ('easting', models.DecimalField(blank=True, db_column='EASTING', decimal_places=4, max_digits=15, null=True)),
                ('elevation', models.DecimalField(blank=True, db_column='ELEVATION', decimal_places=4, max_digits=15, null=True)),
                ('speed', models.DecimalField(blank=True, db_column='SPEED', decimal_places=2, max_digits=5, null=True)),
                ('gps_reception_timestamp', models.CharField(blank=True, db_column='GPS_RECEPTION_TIMESTAMP', max_length=24, null=True)),
                ('channel_quality_indicator', models.DecimalField(blank=True, db_column='CHANNEL_QUALITY_INDICATOR', decimal_places=0, max_digits=7, null=True)),
                ('gps_quality_indicator', models.DecimalField(blank=True, db_column='GPS_QUALITY_INDICATOR', decimal_places=0, max_digits=1, null=True)),
                ('num_of_satellites_in_use', models.DecimalField(blank=True, db_column='NUM_OF_SATELLITES_IN_USE', decimal_places=0, max_digits=3, null=True)),
                ('horizontal_dilution_of_position', models.DecimalField(blank=True, db_column='HORIZONTAL_DILUTION_OF_POSITION', decimal_places=5, max_digits=10, null=True)),
                ('age_of_diff_reference_station', models.DecimalField(blank=True, db_column='AGE_OF_DIFF_REFERENCE_STATION', decimal_places=0, max_digits=7, null=True)),
                ('mdt_msg_generation_timestamp', models.CharField(blank=True, db_column='MDT_MSG_GENERATION_TIMESTAMP', max_length=24, null=True)),
                ('location_sname', models.CharField(blank=True, db_column='LOCATION_SNAME', max_length=24, null=True)),
                ('equip_status_rec_ident', models.DecimalField(blank=True, db_column='EQUIP_STATUS_REC_IDENT', decimal_places=0, max_digits=9, null=True)),
                ('heading', models.DecimalField(blank=True, db_column='HEADING', decimal_places=2, max_digits=5, null=True)),
                ('link_mac_address', models.CharField(blank=True, db_column='LINK_MAC_ADDRESS', max_length=17, null=True)),
                ('previous_latency', models.IntegerField(blank=True, db_column='PREVIOUS_LATENCY', null=True)),
            ],
            options={
                'db_table': 'EQUIP_COORD_TRANS',
                'managed': False,
            },
        ),
    ]
