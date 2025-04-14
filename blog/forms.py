# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Comment

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)