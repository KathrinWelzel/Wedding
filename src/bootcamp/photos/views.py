from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from photologue.models import Photo, Gallery
from photologue.views import PhotoDetailView
from .models import PhotoExtended
from django.contrib.auth.decorators import login_required
from bootcamp.decorators import ajax_required

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'slug', 'caption', 'image']

class GalleryForm(ModelForm):
    class Meta:
        model = Gallery
        fields = ['title', 'slug', 'description']


class AddPhotoView(FormView):
    template_name = 'photo_form.html'
    form_class = PhotoForm
    success_url = '/photos/photo/'

    def form_valid(self, form):
        new_photo = form.save()
        return HttpResponseRedirect(self.get_success_url() + new_photo.slug)

class AddGalleryView(FormView):
    template_name = 'gallery_form.html'
    form_class = GalleryForm
    success_url = '/photos/'

    def form_valid(self, form):
        new_gallery = form.save()
        return HttpResponseRedirect(self.get_success_url())


# TODO: Remove logging, when done
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger("__name__")

# TODO: accept posted picture
@login_required
@ajax_required
def post(request):
    logger.error(str(request.POST))
    logger.error(str(request.user))
    #print("test")
    #last_feed = request.POST.get('last_feed')
    user = request.user
    csrf_token = str(csrf(request)['csrf_token'])
    #feed = Feed()
    #feed.user = user
    post = request.POST['post']
    post = post.strip()
    #if len(post) > 0:
    #    feed.post = post[:255]
    #    feed.save()
    #html = _html_feeds(last_feed, user, csrf_token)
    return HttpResponseRedirect("/")
