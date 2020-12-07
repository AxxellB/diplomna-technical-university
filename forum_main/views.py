from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from forum_main.forms import CreatePostForm
from forum_main.models import Post


def forum_view(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, context=context, template_name='forum/forum.html')


@login_required
def create_post(request):
    if request.method == 'GET':
        context = {
            'form': CreatePostForm
        }
    else:
        form = CreatePostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('index')
        context = {
            'form': form
        }

    return render(request, context=context, template_name='forum/create_thread.html')


@login_required
def my_threads(request):
    if request.method == 'GET':
        user = request.user
        my_posts = Post.objects.filter(user=user)
        show_buttons = True
        context = {
            'posts': my_posts,
            'show_buttons': show_buttons
        }
        return render(request, context=context, template_name='forum/my_threads.html')


def edit_post(request, pk):
    current_post = Post.objects.get(pk=pk)
    if request.method == 'GET':
        form = CreatePostForm(instance=current_post)
        context = {
            'form': form
        }
    else:
        form = CreatePostForm(request.POST, instance=current_post)
        if form.is_valid():
            form.save()
            return redirect('my threads')
        context = {
            'form': form
        }

    return render(request, context=context, template_name='forum/edit_thread.html')


def delete_post(request, pk):
    current_post = Post.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, template_name='forum/delete_thread.html')
    else:
        current_post.delete()
        return redirect('my threads')
