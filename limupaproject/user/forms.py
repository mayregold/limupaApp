from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    USER_TYPES = [
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
    ]
    user_type = forms.ChoiceField(choices=USER_TYPES, widget=forms.RadioSelect)
 
    class Meta:
        model = User
        fields = ['username','email','password1','password2','user_type']

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            user.profile.user_type = self.cleaned_data['user_type']
            user.profile.save()
        return user        
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user_type', 'profile_pic', 'bio', 'location']

    def _init_(self, *args, **kwargs):
        super(ProfileForm, self)._init_(*args, **kwargs)
        self.fields['profile_pic'].required = False  # Make the profile picture optional

        