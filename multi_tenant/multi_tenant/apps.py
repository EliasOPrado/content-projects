from django.apps import AppConfig


class MultiTenantConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'multi_tenant'
