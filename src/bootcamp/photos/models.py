from django.db import models
from django.contrib.auth.models import User
from photologue.models import Photo
from taggit.managers import TaggableManager

class PhotoExtended(models.Model):
    photo = models.OneToOneField(Photo, related_name='extended')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    tags = TaggableManager(blank=True)

    class Meta:
        verbose_name = u'Extra fields'
        verbose_name_plural = u'Extra fields'

    def __str__(self):
        return self.photo.title
