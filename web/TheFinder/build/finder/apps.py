from django.apps import AppConfig
import os

class FinderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'finder'
    has_run = False

    def ready(self):
        if not FinderConfig.has_run:
            FinderConfig.has_run = True
            print("the application is running")