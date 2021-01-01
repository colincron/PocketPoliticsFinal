from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import StandardUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = StandardUser
        fields = ('username', 'email', 'dob', 'address1', 'address2', 'city', 'state', 'zip_code', 'pol_preference')
