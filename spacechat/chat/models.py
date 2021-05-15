from django.db import models

try:
    from django.db.models import JSONField
except ImportError:
    from django.contrib.postgres.fields import JSONField

class Room(models.Model):
     
    title = models.CharField(max_length=255, default="")
    
    desc = models.CharField(max_length=255, default="")
    
    staff_only = models.BooleanField(default=False)
        
    my_json = models.JSONField(default=dict, blank=True)
    counter = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

    @property
    def group_name(self):
       
        return "room-%s" % self.id
