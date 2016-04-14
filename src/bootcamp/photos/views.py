from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from photologue.models import Photo, Gallery
from photologue.views import PhotoDetailView
from .models import PhotoExtended

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
