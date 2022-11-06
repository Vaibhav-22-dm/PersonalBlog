from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(Blog)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
    def get_form(self, request, obj=None, **kwargs):
        if not request.user.is_superuser:
            self.exclude = ("author", )
        form = super(BlogAdmin, self).get_form(request, obj, **kwargs)
        return form

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)
