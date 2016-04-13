from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from photologue.models import Photo
from photologue.views import PhotoDetailView
from .models import PhotoExtended

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'slug', 'caption', 'image']


class AddPhotoView(FormView):
    template_name = 'photologue/photo_form.html'
    form_class = PhotoForm
    success_url = '/photos/photo/'

    def form_valid(self, form):
        new_photo = form.save()
        return HttpResponseRedirect(self.get_success_url() + new_photo.slug)
