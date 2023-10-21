from django.db import models

class Announcement(models.Model):
    '''
    Defines the announcements issued to the school 
    and the masses
    '''
    headline = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    date_issued = models.DateTimeField(auto_now_add=True)  # When first created
