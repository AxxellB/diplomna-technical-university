from django.urls import path

from forum_main.views import forum_view, create_post, my_threads, edit_post, delete_post

urlpatterns = [
    path('', forum_view, name='index'),
    path('create/', create_post, name='create post'),
    path('my_threads/', my_threads, name='my threads'),
    path('edit/<int:pk>/', edit_post, name='edit post'),
    path('delete/<int:pk>/', delete_post, name='delete post')
]