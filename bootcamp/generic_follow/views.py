"""Views for the ``followit`` app,
all are ajax views and return application/json mimetype
"""
from .utils import ajax_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from bootcamp.activities.models import Activity
from django.http import HttpResponse, HttpResponseForbidden
import json

# @utils.follow_ajax_view
# @utils.post_only
# def follow_object(request, app = None, model = None, object_id = None):
#     """follows an object and returns status:
#     * 'success' - if an object was successfully followed
#     * the decorator takes care of the error situations
#     """
#     model_obj = apps.get_model(app, model)
#     obj = model.objects.get(pk=object_id)
#     request.user.follow(obj)
#     return {'status': 'success'}
#
#
# @utils.follow_ajax_view
# @utils.post_only
# def unfollow_object(request, app = None, model = None, object_id = None):
#     """unfollows an object and returns status 'success' or
#     'error' - via the decorator :func:`~followit.utils.followit_ajax_view`
#     """
#     model_obj = apps.get_model(app, model)
#     obj = model.objects.get(pk=object_id)
#     unfollow_func = getattr(request.user, 'unfollow_' + model_name)
#     request.user.unfollow(obj)
#     return {'status': 'success'}
#
#
# @utils.follow_ajax_view
# @utils.post_only
# def toggle_follow_object(request, app = None, model = None, object_id = None):
#     """if object is followed then unfollows
#     otherwise follows
#
#     returns json
#     {
#         'status': 'success', # or 'error'
#         'following': True, #or False
#     }
#
#
#     unfollows an object and returns status 'success' or
#     'error' - via the decorator :func:`~followit.utils.followit_ajax_view`
#     """
#     model_obj = apps.get_model(app, model)
#     obj = model.objects.get(pk=object_id)
#     if request.user.is_following(obj):
#         request.user.unfollow(obj)
#         following = False
#     else:
#         request.user.follow(obj)
#         following = True
#
#     return {
#         'status': 'success',
#         'following': following
#     }

@login_required
@ajax_required
def follow_user(request):
    page_user_id = request.POST['page_user_id']
    page_user = User.objects.get(id=page_user_id)
    user = request.user
    if user.is_following(page_user):
        user.unfollow(page_user)
        user.profile.unotify_following(page_user)
        data = {'status': 'not_following'}
    else:
        user.follow(page_user)
        user.profile.notify_following(page_user)
        data = {'status': 'following'} #TODO question.calculate_favorites()
    return HttpResponse(json.dumps(data), content_type='application/json')
