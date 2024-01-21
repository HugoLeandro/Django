from django.apps import AppConfig
from .config import EMAIL_ADMIN, SENHA_ADMIN

class FilmeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "filme"

    def ready(self):
        from .models import Usuario

        usuarios = Usuario.objects.filter(email=EMAIL_ADMIN)
        if not usuarios:
            Usuario.objects.create_superuser(username="admin", email=EMAIL_ADMIN, password=SENHA_ADMIN, is_active=True, is_staff=True)
