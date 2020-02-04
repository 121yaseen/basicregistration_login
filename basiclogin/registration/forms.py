from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from registration.models import User

class Registration(UserCreationForm):
      def __init__(self, *args, **kwargs):
        super(Registration, self).__init__(*args, **kwargs)
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"
      class meta:
        model = User
        fields = ['email', 'password1', 'password2']
      def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        if commit:
            user.save()
        return user
