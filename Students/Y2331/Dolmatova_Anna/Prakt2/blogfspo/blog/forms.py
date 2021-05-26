from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CarOwnerForm(forms.ModelForm):
    class Meta:

        model = CarOwner

        fields = '__all__'



