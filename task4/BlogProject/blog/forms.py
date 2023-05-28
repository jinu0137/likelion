from django import forms
from .models import Blog

class BlogForm(forms.Form):
    class Meta:
        model = Blog
        fields = ('owner', 'title', 'description')
