from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

class Message(models.Model):
    # Can access Room and user with Message but not other way around(doesn't make sense),
    #  but we can query all messages using room and user
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)   
    # when Room is deleted, also delete the messages
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # This just instructs the DB to order messages by date_added
    class Meta:
        ordering = ('date_added', )
