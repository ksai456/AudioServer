from django.db import models
import datetime
from django.core.exceptions import ValidationError
import pytz

utc=pytz.UTC

   
def validate_date(value):
    pass
    # if value != utc.localize(datetime.datetime.today()):
    #     raise ValidationError("The date cannot be in the past!")
    # return value

class audioTime(models.Model):
    duration_in_number_of_seconds = models.IntegerField()
    uploaded_time = models.DateTimeField(validators=[validate_date])
    audiofiletype = models.CharField(max_length = 10)
    class Meta:
        abstract = True
        
class Song(audioTime):
    name_of_the_song = models.CharField(max_length=100)
    
    
class Podcast(audioTime):
    name_of_the_podcast = models.CharField(max_length=100)
    host = models.CharField(max_length=100)
    participants = models.CharField(max_length=100)

    
class Audiobook(audioTime):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    narrator = models.CharField(max_length = 100)
    
audiofiletype = {"song": Song, "audiobook": Audiobook, "podcast": Podcast}

    
    
    

