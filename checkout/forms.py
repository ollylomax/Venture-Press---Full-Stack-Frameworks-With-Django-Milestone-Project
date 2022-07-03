from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        # widgets = {
        #     'has_artwork': forms.HiddenInput(),
        # }
        fields = ('full_name', 'email', 'phone_number',
                  'address_line1', 'address_line2',
                  'city', 'postcode', 'country',
                  'county', 'has_artwork')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Post Code',
            'city': 'City',
            'address_line1': 'Address Line 1',
            'address_line2': 'Address Line 2',
            'county': 'County',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        
        for field in self.fields:
            if field != 'has_artwork':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'stripe-style-input'
                self.fields[field].label = False