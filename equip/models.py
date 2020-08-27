# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Equip(models.Model):
    equip_ident = models.CharField(
        db_column='EQUIP_IDENT', primary_key=True, max_length=6)
    name = models.CharField(
        db_column='NAME', max_length=24, blank=True, null=True)
    descrip = models.CharField(
        db_column='DESCRIP', max_length=35, blank=True, null=True)
    eqp_type = models.CharField(
        db_column='EQP_TYPE', max_length=3, blank=True, null=True)
    fleet_ident = models.CharField(
        db_column='FLEET_IDENT', max_length=3, blank=True, null=True)
    chklist_ident = models.IntegerField(
        db_column='CHKLIST_IDENT', blank=True, null=True)
    fuel_normal_hour = models.DecimalField(
        db_column='FUEL_NORMAL_HOUR', max_digits=6, decimal_places=1, blank=True, null=True)
    fuel_fill_hour = models.DecimalField(
        db_column='FUEL_FILL_HOUR', max_digits=6, decimal_places=1, blank=True, null=True)
    fuel_critical = models.DecimalField(
        db_column='FUEL_CRITICAL', max_digits=6, decimal_places=1, blank=True, null=True)
    fuel_capacity = models.DecimalField(
        db_column='FUEL_CAPACITY', max_digits=6, decimal_places=1, blank=True, null=True)
    gps_flag = models.CharField(
        db_column='GPS_FLAG', max_length=1, blank=True, null=True)
    mdt_flag = models.CharField(
        db_column='MDT_FLAG', max_length=1, blank=True, null=True)
    smu_flag = models.CharField(
        db_column='SMU_FLAG', max_length=1, blank=True, null=True)
    serial_number = models.CharField(
        db_column='SERIAL_NUMBER', max_length=40, blank=True, null=True)
    model_number = models.CharField(db_column='MODEL_NUMBER', max_length=40,
                                    blank=True, null=True)  
    manufacturer = models.CharField(db_column='MANUFACTURER', max_length=15,
                                    blank=True, null=True)  
    business_unit = models.DecimalField(
        db_column='BUSINESS_UNIT', max_digits=6, decimal_places=0, blank=True, null=True)
    owner = models.CharField(
        db_column='OWNER', max_length=20, blank=True, null=True)
    manufacturer_date = models.CharField(
        db_column='MANUFACTURER_DATE', max_length=50, blank=True, null=True)
    wenco_entry_date = models.CharField(
        db_column='WENCO_ENTRY_DATE', max_length=50, blank=True, null=True)
    cost_code = models.CharField(
        db_column='COST_CODE', max_length=5, blank=True, null=True)
    workorder = models.CharField(
        db_column='WORKORDER', max_length=8, blank=True, null=True)
    ani = models.DecimalField(
        db_column='ANI', max_digits=5, decimal_places=0, blank=True, null=True)
    ip_address = models.CharField(
        db_column='IP_ADDRESS', max_length=15, blank=True, null=True)
    ip_port = models.DecimalField(
        db_column='IP_PORT', max_digits=6, decimal_places=0, blank=True, null=True)
    eqmodel_code = models.CharField(db_column='EQMODEL_CODE', max_length=15,
                                    blank=True, null=True)  
    hide_from_fleet_control = models.CharField(
        db_column='HIDE_FROM_FLEET_CONTROL', max_length=1, blank=True, null=True)
    active = models.CharField(
        db_column='ACTIVE', max_length=1, blank=True, null=True)
    test = models.CharField(
        db_column='TEST', max_length=1, blank=True, null=True)
    device_name = models.CharField(
        db_column='DEVICE_NAME', max_length=32, blank=True, null=True)
    os_version = models.CharField(
        db_column='OS_VERSION', max_length=12, blank=True, null=True)
    mdt_version = models.CharField(
        db_column='MDT_VERSION', max_length=12, blank=True, null=True)
    dmp_address = models.CharField(
        db_column='DMP_ADDRESS', max_length=8, blank=True, null=True)
    channel = models.DecimalField(
        db_column='CHANNEL', max_digits=2, decimal_places=0, blank=True, null=True)
    comment = models.CharField(
        db_column='COMMENT', max_length=255, blank=True, null=True)
    mdt_text = models.CharField(
        db_column='MDT_TEXT', max_length=35, blank=True, null=True)
    v2x_mac_address = models.CharField(
        db_column='V2X_MAC_ADDRESS', max_length=17, blank=True, null=True)
    next_inspection_alert_smu_hours = models.FloatField(
        db_column='NEXT_INSPECTION_ALERT_SMU_HOURS', blank=True, null=True)  
    next_inspection_alert_traveled_distance = models.FloatField(
        db_column='NEXT_INSPECTION_ALERT_TRAVELED_DISTANCE', blank=True, null=True)  


    class Meta:
        managed = False
        db_table = 'EQUIP'


class EquipCoordTrans(models.Model):
    timestamp = models.CharField(
        db_column='TIMESTAMP', primary_key=True, max_length=24)
    equip_ident = models.CharField(db_column='EQUIP_IDENT', max_length=6)  
    shift_date = models.CharField(
        db_column='SHIFT_DATE', max_length=24, blank=True, null=True)
    shift_ident = models.CharField(
        db_column='SHIFT_IDENT', max_length=1, blank=True, null=True)
    northing = models.DecimalField(
        db_column='NORTHING', max_digits=15, decimal_places=4, blank=True, null=True)
    easting = models.DecimalField(
        db_column='EASTING', max_digits=15, decimal_places=4, blank=True, null=True)
    elevation = models.DecimalField(
        db_column='ELEVATION', max_digits=15, decimal_places=4, blank=True, null=True)
    speed = models.DecimalField(
        db_column='SPEED', max_digits=5, decimal_places=2, blank=True, null=True)
    gps_reception_timestamp = models.CharField(
        db_column='GPS_RECEPTION_TIMESTAMP', max_length=24, blank=True, null=True)
    channel_quality_indicator = models.DecimalField(
        db_column='CHANNEL_QUALITY_INDICATOR', max_digits=7, decimal_places=0, blank=True, null=True)  
    gps_quality_indicator = models.DecimalField(
        db_column='GPS_QUALITY_INDICATOR', max_digits=1, decimal_places=0, blank=True, null=True)
    num_of_satellites_in_use = models.DecimalField(
        db_column='NUM_OF_SATELLITES_IN_USE', max_digits=3, decimal_places=0, blank=True, null=True)
    horizontal_dilution_of_position = models.DecimalField(
        db_column='HORIZONTAL_DILUTION_OF_POSITION', max_digits=10, decimal_places=5, blank=True, null=True)  
    age_of_diff_reference_station = models.DecimalField(
        db_column='AGE_OF_DIFF_REFERENCE_STATION', max_digits=7, decimal_places=0, blank=True, null=True)
    mdt_msg_generation_timestamp = models.CharField(
        db_column='MDT_MSG_GENERATION_TIMESTAMP', max_length=24, blank=True, null=True)  
    location_sname = models.CharField(
        db_column='LOCATION_SNAME', max_length=24, blank=True, null=True)
    equip_status_rec_ident = models.DecimalField(
        db_column='EQUIP_STATUS_REC_IDENT', max_digits=9, decimal_places=0, blank=True, null=True)  
    heading = models.DecimalField(
        db_column='HEADING', max_digits=5, decimal_places=2, blank=True, null=True)
    link_mac_address = models.CharField(
        db_column='LINK_MAC_ADDRESS', max_length=17, blank=True, null=True)
    previous_latency = models.IntegerField(
        db_column='PREVIOUS_LATENCY', blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'EQUIP_COORD_TRANS'
        unique_together = (('timestamp', 'equip_ident'),)
