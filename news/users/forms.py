from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser1


class CustomUserCreationForm1(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser1
        fields = UserCreationForm.Meta.fields

class CustomUserChangeForm1(UserChangeForm):

    class Meta:
        model = CustomUser1
        fields = UserChangeForm.Meta.fields