from django.db import models

class HolidayMaster(models.Model):
    holiday_id   = models.AutoField(primary_key=True)
    employee_id  = models.IntegerField(blank=True, null=True)
    holiday      = models.DateTimeField(blank=True, null=True)

    author       = models.IntegerField(blank=True, null=True)
    create_time  = models.DateTimeField(blank=True, null=True, auto_now=False, auto_now_add=True)
    updater      = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True, auto_now=True, auto_now_add=False)

    class Meta:
        managed  = True
        db_table = 'holiday_master'
