from django.db import models
from enzemi.models.major_classification_master import MajorClassificationMaster
from enzemi.models.small_classification_master import SmallClassificationMaster

class NightTaskMaster(models.Model):
    task_id                 = models.AutoField(primary_key=True)
    employee_id             = models.IntegerField(blank=True, null=True)
    task_name               = models.CharField(blank=True, null=True, max_length=100)
    major_classification = models.ForeignKey(MajorClassificationMaster)
    small_classification = models.ForeignKey(SmallClassificationMaster)
    importance              = models.CharField(blank=True, null=True, max_length=100)
    start_time              = models.DateTimeField(blank=True, null=True)
    finish_time             = models.DateTimeField(blank=True, null=True)
    situation               = models.CharField(blank=True, null=True, max_length=100)

    author                  = models.IntegerField(blank=True, null=True)
    create_time             = models.DateTimeField(blank=True, null=True, auto_now=False, auto_now_add=True)
    updater                 = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True, auto_now=True, auto_now_add=False)
    
    class Meta:
        managed  = True
        db_table = 'night_task_master'
