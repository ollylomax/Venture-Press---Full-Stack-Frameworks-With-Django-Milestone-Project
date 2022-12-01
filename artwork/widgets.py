from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """
    Custom widget inheriting the Clearable File Input widget from django.
    Set template to the custom widget html page in new template directory.
    """
    template_name = (
        'artwork/custom_widget_templates/custom_clearable_file_input.html'
    )
