from django.db import models

# Create your models here.
class Url(models.Model):
    link = models.CharField(max_length=1000000000000000)
    uuid = models.CharField(max_length=10)
    
    def __str__(self):
        return self.uuid
    