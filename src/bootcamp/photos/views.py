from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from photologue.models import Photo
from .models import PhotoExtended

class AddPhotoView(CreateView):
    model = Photo
    fields = ['title', 'slug', 'caption', 'image']
