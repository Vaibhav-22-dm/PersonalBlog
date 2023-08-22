from django.apps import AppConfig


class BlogsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Blogs'

    def ready(self):
        from actstream import registry
        from django.contrib.auth.models import User
        registry.register(User,self.get_model('Blog'))