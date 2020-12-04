from django.contrib.auth import logout
from django.shortcuts import render, redirect


# Create your views here.
from forum_auth.forms import RegisterForm, LoginForm


def register_user(request):
    if request.method == 'GET':
        context = {
            'form': RegisterForm
        }
        return render(request, context=context, template_name='auth/register.html')
    else:
        pass


def login_user(request):
    if request.method == 'GET':
        context = {
            'form': LoginForm
        }
        return render(request, context=context, template_name='auth/login.html')
    else:
        pass


def logout_user(request):
    logout(request)
    return redirect('index')

