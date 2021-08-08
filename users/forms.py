from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import CustomUser
from .models import Profile

class SignUpForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name'] 


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio'] 