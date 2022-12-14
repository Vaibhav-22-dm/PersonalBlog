from django.forms import ModelForm
from django import forms
from .models import Blog

class BlogCreationForm(ModelForm):
    title = forms.CharField(widget=forms.Textarea, required=True)
    content = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = Blog
        exclude = ['author']