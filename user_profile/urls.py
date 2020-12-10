from django.urls import path

from user_profile.views import user_profile

urlpatterns = [
    path('user/<str:user>', user_profile, name='user profile')
]