from django import forms
from .models import Service, Category
from .widgets import CustomClearableFileInput


class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    
    def __init__(self, *args, **kwargs):
        # Overwrite init method to make changes to fields
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        # List comprehension to create list of tuples of friendly names associated with their category ids
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        # Update category field on form to use friendly names for choices instead of id
        self.fields['category'].choices = friendly_names
        # Iterate through rest of the fields to apply class
        # for field_name, field in self.fields.items():
        #     field.widget.attrs['class'] = 'border-black rounded-0'