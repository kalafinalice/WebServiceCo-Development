from django.db import models
from enzemi.models.major_classification_master import MajorClassificationMaster

class SmallClassificationMaster(models.Model):
    small_classification_id = models.AutoField(primary_key=True)
    small_classification    = models.CharField(blank=True, max_length=100)
    major_classification = models.ForeignKey(MajorClassificationMaster)

    author                  = models.IntegerField(blank=True, null=True)
    create_time             = models.DateTimeField(blank=True, null=True, auto_now=False, auto_now_add=True)
    updater                 = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True, auto_now=True, auto_now_add=False)

    def __str__(self):
            return self.small_classification

    class Meta:
        managed  = True
        db_table = 'small_classification_master'
