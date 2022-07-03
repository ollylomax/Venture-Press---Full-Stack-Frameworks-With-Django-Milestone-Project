from django import forms


class ArtworkUpload(forms.Form):
    upload = forms.FileField(label='Upload Artwork')