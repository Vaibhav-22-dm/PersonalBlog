from django.forms import ModelForm
from .models import *
from tinymce.widgets import TinyMCE

class BlogCreationForm(ModelForm):
    class Meta:
        model = Blog
        exclude = ['author']
        widgets = {'content': TinyMCE(attrs={'cols': 80, 'rows': 30})}


class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['author', 'blog', 'reply']