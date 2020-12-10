from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.


@login_required(login_url='login user')
def user_profile(request, user):
    if request.method == 'GET':
        return render(request, 'profile/my_profile.html',)
