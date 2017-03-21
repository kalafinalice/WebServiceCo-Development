from django.db import models

class MajorClassificationMaster(models.Model):
    major_classification_id = models.AutoField(primary_key=True)
    major_classification    = models.CharField(blank=True, max_length=100)

    author                  = models.IntegerField(blank=True, null=True)
    create_time             = models.DateTimeField(blank=True, null=True, auto_now=False, auto_now_add=True)
    updater                 = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True, auto_now=True, auto_now_add=False)

    def __str__(self):
            return self.major_classification
            
    class Meta:
        managed  = True
        db_table = 'major_classification_master'
