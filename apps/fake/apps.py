from django.apps import AppConfig


class FakeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.fake'
