from django.db import models

# Create your models here.


class AudioDb(models.Model):
    audiofile = models.FileField(
        upload_to='audisl/audioFiles/', blank=True, null=True)
    textfile = models.FileField(
        upload_to='audisl/textFiles/', blank=True, null=True)
    imagefile = models.FileField(
        upload_to='audisl/imageFiles/', blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    # Supplementary
    # voice_record = models.FileField()
