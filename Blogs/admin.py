from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title',)

    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser == False:
            self.exclude = ("author", )
        form = super(BlogAdmin, self).get_form(request, obj, **kwargs)
        return form

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser == False:
            obj.author = request.user
        obj.save()

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    readonly_fields = ["content","blog","author"]

    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser == True:
            self.exclude = ("author", )
        form = super(CommentAdmin, self).get_form(request, obj, **kwargs)
        return form

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(blog__author=request.user)

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser == False:
            obj.author = request.user
        obj.save()
