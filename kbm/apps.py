from django.apps import AppConfig


# class CheradipConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'kbm'


class KbmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kbm'

    def ready(self):
        import kbm.signals
