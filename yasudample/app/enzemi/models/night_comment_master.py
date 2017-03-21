from django.db import models

class NightCommentMaster(models.Model):
    comment_id  = models.AutoField(primary_key=True)
    employee_id = models.IntegerField(blank=True, null=True)
    date        = models.DateField(blank=True, null=True)
    comment     = models.CharField(blank=True, null=True, max_length=100)

    author      = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True, auto_now=False, auto_now_add=True)
    updater     = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True, auto_now=True, auto_now_add=False)

    class Meta:
        managed  = True
        db_table = 'night_comment_master'
