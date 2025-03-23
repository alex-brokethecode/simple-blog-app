from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_created', 'date_updated',)
    list_filter = ('date_created', 'author__username', )
    search_fields = ('author', 'title',)


"""
Step 7: User Authentication
- Set up Django's authentication system for login, logout, and registration.
- Restrict post creation/editing to logged-in users only.

Step 8: Extra Features (Optional, but Recommended!)

- Add pagination to the blog post list.
- Implement a search feature.
- Allow users to comment on posts.
"""
