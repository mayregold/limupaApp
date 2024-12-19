from user.models import Profile  # Ensure this points to the correct Profile model

def profile_picture(request):
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
            return {'profile_picture': profile.profile_pic}  # Updated to match the field name
        except Profile.DoesNotExist:
            return {'profile_picture': None}
    return {'profile_picture': None}
