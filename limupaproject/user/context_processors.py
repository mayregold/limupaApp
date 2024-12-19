from user.models import Profile

def add_profile(request):
    if request.user.is_authenticated:
        return {'profile': request.user.profile}