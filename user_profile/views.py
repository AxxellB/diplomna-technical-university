from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from user_profile.forms import ChangeEmailForm


@login_required(login_url='login user')
def user_profile(request, user):
    change_pass_form = PasswordChangeForm(user)
    change_email_form = ChangeEmailForm(user)

    if request.method == 'POST':
        if 'change_password' in request.POST:
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                login(request, user)
                messages.success(request, 'Your password was successfully updated!')
                return redirect('user profile', request.user)
            else:
                messages.error(request, 'Your password was not changed! Please fix the errors!')
                context = {
                    'change_pass_form': form,
                    'change_email_form': change_email_form
                }
        else:
            form = ChangeEmailForm(request.user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your email was successfully updated!')
                return redirect('user profile', request.user)
            else:
                messages.error(request, 'Your email was not changed! Please fix the errors below!')
                context = {
                    'change_pass_form': change_pass_form,
                    'change_email_form': form
                }
    else:
        context = {
                'change_pass_form': change_pass_form,
                'change_email_form': change_email_form
                }
    return render(request, 'profile/my_profile.html', context)