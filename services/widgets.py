from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    input_text = _('')
    clear_checkbox_label = _('Delete Image')
    initial_text = _('Service Image')
    template_name = 'services/custom_widget_templates/custom_clearable_file_input.html'