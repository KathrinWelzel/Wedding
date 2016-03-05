from django.http import HttpResponseBadRequest, HttpResponseRedirect, HttpResponse
import functools
import json

def follow_ajax_view(view_func):
    """decorator that does certain error checks on the input
    and serializes response as json

    in the case of error, json output will contain
    """
    @functools.wraps(view_func)
    def wrapped_view(request, app = None, model = None, object_id = None):
        try:
            assert(request.user.is_authenticated())
            assert(request.method == 'POST')
            assert(request.is_ajax())
            data = view_func(request, app, model, object_id)
        except Exception as e:
            data = {'status': 'error', 'error_message': str(e)}

        return HttpResponse(json.dumps(data), content_type='application/json')
    return wrapped_view

def post_only(view_func):
    """simple decorator raising assertion error when method is not 'POST"""
    @functools.wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        assert(request.method == 'POST')
        return view_func(request, *args, **kwargs)
    return wrapped_view
