from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from . import models

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        


class AddRecordForm(forms.ModelForm):
    class Meta:
        model = models.Record
        fields = "__all__"
        exclude = ["id", "createed_at"]