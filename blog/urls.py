from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('post-create/', views.post_create, name='post_create'),
    path('post-details/<int:pk>', views.post_details, name='post_details'),
    path('post-update/<int:pk>', views.post_update, name='post_update'),
    path('post-delete/<int:pk>', views.post_delete, name='post_delete'),
]
