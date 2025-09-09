
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignupForm(UserCreationForm):
    role = forms.ChoiceField(choices=User.ROLE_CHOICES, label='Role')
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ('username','email','role','password1','password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = self.cleaned_data.get('role', User.PATIENT)
        user.email = self.cleaned_data.get('email', '') or ''
        if commit:
            user.save()
        return user
