from django import forms
from .models import UserProfile

from allauth.account.forms import ChangePasswordForm, SignupForm, LoginForm


class CustomChangePasswordForm(ChangePasswordForm):
    def __init__(self, *args, **kwargs):
        super(CustomChangePasswordForm, self).__init__(*args, **kwargs)

        placeholders = {
            'oldpassword': 'Enter Current Password',
            'password1': 'Enter New Password',
            'password2': 'Confirm New Password',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False


class CustomRegisterForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(CustomRegisterForm, self).__init__(*args, **kwargs)

        placeholders = {
            'email': 'Enter Email',
            'email2': 'Confirm Email',
            'username': 'Enter Username',
            'password1': 'Enter Password',
            'password2': 'Confirm Password',
        }
        
        self.fields['email'].widget.attrs['autofocus'] = True

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)

        placeholders = {
            'login': 'Enter Username or Email',
            'password': 'Enter Password',
        }

        for field in self.fields:
            if field != 'remember':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'stripe-style-input'
                self.fields[field].label = False

        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'default_address_line1': 'Street Address 1',
            'default_address_line2': 'Street Address 2',
            'default_city': 'City',
            'default_county': 'County',
            'default_postcode': 'Postal Code',
            'default_phone_number': 'Phone Number',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False