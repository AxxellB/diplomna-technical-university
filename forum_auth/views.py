from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
from forum_auth.forms import RegisterForm, LoginForm


def register_user(request):
    if request.method == 'GET':
        context = {
            'form': RegisterForm
        }
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        context = {
            'form': form
        }

    return render(request, context=context, template_name='auth/register.html')


def login_user(request):
    if request.method == 'GET':
        context = {
            'form': LoginForm
        }
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Incorrect username or password!')
        context = {
            'form': form
        }

    return render(request, context=context, template_name='auth/login.html')


@login_required
def logout_user(request):
    logout(request)
    return redirect('index')

