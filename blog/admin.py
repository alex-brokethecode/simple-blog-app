from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_created', 'date_updated',)
    list_filter = ('date_created', 'author__username', )
    search_fields = ('author', 'title',)
