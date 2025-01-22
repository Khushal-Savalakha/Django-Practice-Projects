# from django.apps import AppConfig


# class MyappConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'myapp'
#     def ready(self):
#         import myapp.signals

from django.apps import AppConfig

class MyappConfig(AppConfig):
    """
    Configuration for the 'myapp' application.
    Automatically imports signal handlers when the application is ready.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        """
        Import signal handlers for the 'myapp' application when it's ready.
        """
        import myapp.signals
