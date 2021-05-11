from django.db import models

try:
    from django.db.models import JSONField
except ImportError:
    from django.contrib.postgres.fields import JSONField

class Room(models.Model):
    """
    A room for people to chat in.
    """
    default_auto_field = 'django.db.models.AutoField'
    #id = models.AutoField(primary_key=True)

    # Chat title/name
    title = models.CharField(max_length=255, default="")
    
    # Chat description
    desc = models.CharField(max_length=255, default="")
    
    # If only "staff" users are allowed (is_staff on django's User)
    staff_only = models.BooleanField(default=False)
        
    my_json = models.JSONField(default={}, blank=True)
    counter = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

    @property
    def group_name(self):
        """
        Returns the Channels Group name that sockets should subscribe to to get sent
        messages as they are generated.
        """
        return "room-%s" % self.id
