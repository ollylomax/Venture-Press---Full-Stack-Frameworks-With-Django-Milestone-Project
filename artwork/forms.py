from django import forms
from .models import Artwork
from .widgets import CustomClearableFileInput


class ArtworkUpload(forms.ModelForm):
    class Meta:
        model = Artwork
        widgets = {
            'user': forms.HiddenInput(),
            'order': forms.HiddenInput(),
        }
        fields = ('user', 'order', 'upload')
    
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        
        self.fields['upload'].label = False
    
    upload = forms.FileField(label='Upload Artwork', widget=CustomClearableFileInput)
    # image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)