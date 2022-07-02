from django import forms
from .models import Messages


class ContactForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ('first_name', 'last_name', 'email', 'subject', 'message')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'message': 'Your Message',
        }

        for field in self.fields:
            if field != 'subject':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]}*'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].label = False
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            