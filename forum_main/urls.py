from django.urls import path

from forum_main.views import forum_view

urlpatterns = [
    path('', forum_view, name='forum')
]