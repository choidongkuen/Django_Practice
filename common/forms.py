from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# UserCreationForm : 1. username 2. password1 3. password2
# + email
class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "email")
