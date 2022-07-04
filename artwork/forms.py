from django import forms
from .models import Artwork


class ArtworkUpload(forms.ModelForm):
    class Meta:
        model = Artwork
        widgets = {
            'user': forms.HiddenInput(),
            'order': forms.HiddenInput(),
        }
        fields = ('user', 'order', 'upload')
        
    upload = forms.FileField(label='Upload Artwork')