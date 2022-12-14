from django.forms import ModelForm
from .models import Blog

class BlogCreationForm(ModelForm):
    class Meta:
        model = Blog
        exclude = ['author']