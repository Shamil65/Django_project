from django import forms
from .models import Cats


class ImageForm(forms.ModelForm):
    class Meta:
        model = Cats
        fields = ('title', 'image')
