from django import forms
from .models import Artwork
from .widgets import CustomClearableFileInput


class ArtworkUpload(forms.ModelForm):
    """
    Form class importing the ArtworkUpload model, hiding user and order fields
    using widgets and remove label from upload field. Set upload filefield
    variable to use custom clearable file input widget from imported widgets.
    """
    class Meta:
        model = Artwork
        widgets = {
            'user': forms.HiddenInput(),
            'order': forms.HiddenInput(),
        }
        fields = ('user', 'order', 'upload')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['upload'].label = False

    upload = forms.FileField(
        label='Upload Artwork', widget=CustomClearableFileInput)
