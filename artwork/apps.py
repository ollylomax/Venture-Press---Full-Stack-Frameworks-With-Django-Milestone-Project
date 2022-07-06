from django.apps import AppConfig


class ArtworkConfig(AppConfig):
    """
    Load artwork configuration.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'artwork'
