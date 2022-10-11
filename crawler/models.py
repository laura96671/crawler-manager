from django.db import models


class CrawlerManager(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=10)
    url = models.CharField(max_length=255, blank=True, null=True)
    params = models.JSONField(blank=True, null=True)
    created_by = models.CharField(max_length=50)
    created_on = models.DateTimeField()
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=50, blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crawler_manager'
