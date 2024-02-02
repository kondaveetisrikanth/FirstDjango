from django.forms import ModelForm

from .models import UserDetails

class UserForm(ModelForm):
    class Meta:
        model=UserDetails