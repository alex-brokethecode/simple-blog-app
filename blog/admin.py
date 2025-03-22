from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_created', 'date_updated',)
    list_filter = ('date_created', 'author__username', )
    search_fields = ('author', 'title',)


"""
Step 5: Create Views and URLs
Implement views for:

- List all posts (home page).
- View a single post (detail page).
- Create a post (only for logged-in users).
- Update & delete a post (only by the post author).
- Define corresponding URLs in urls.py.

Step 6: Implement Templates

- Use Django's template system to display the blog pages.
- Create a base template for common UI elements (navbar, footer).
- Style the pages using basic CSS (or Bootstrap).

Step 7: User Authentication
- Set up Django's authentication system for login, logout, and registration.
- Restrict post creation/editing to logged-in users only.

Step 8: Extra Features (Optional, but Recommended!)

- Add pagination to the blog post list.
- Implement a search feature.
- Allow users to comment on posts.
"""
