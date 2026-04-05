from django.contrib import admin

# Register your models here.

from .models import Blog

class BlogAdmin(admin.ModelAdmin):

    list_display = ('title','created_at')

    prepopulated_fields = {'slug':('title',)}

    search_fields = ('title',)

admin.site.register(Blog,BlogAdmin)