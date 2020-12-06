from django.urls import path

from forum_main.views import forum_view, create_post

urlpatterns = [
    path('', forum_view, name='index'),
    path('create/', create_post, name='create post')
]