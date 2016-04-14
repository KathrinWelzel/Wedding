from django.conf.urls import patterns, include, url
from django.views.generic import CreateView
from photologue.models import Photo
from photologue.views import GalleryListView
from .views import AddPhotoView, AddGalleryView

urlpatterns = patterns('bootcamp.photos.views',
    #url(r'^$', 'photos', name='photos'),
    url(r'^$', GalleryListView.as_view(paginate_by=5), name='photos'),
    url(r'^add/$', AddPhotoView.as_view() , name='add'),
    url(r'^addGallery/$', AddGalleryView.as_view() , name='addGallery'),
    url(r'^', include('photologue.urls', namespace='photologue'), name='photos'),
    #url(r'^(\d+)/$', 'photos', name='photos'),
)
