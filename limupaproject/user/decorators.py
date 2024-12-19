from django.http import HttpResponseForbidden
from functools import wraps


def seller_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if hasattr(request.user, 'Profile')  and request.user.profile.user_type == 'seller':
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("you must be a seller to access this page")
    return _wrapped_view