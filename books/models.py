from django.db import models

class book(models.Model):
    name = models.CharField(max_length=255)
    readCount = models.IntegerField(default=0)
    content = models.TextField(null=True, blank=True)
