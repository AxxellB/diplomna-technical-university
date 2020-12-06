from django.contrib.auth.decorators import login_required
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
            form.save()
            return redirect('index')
        context = {
            'form': form
        }

    return render(request, context=context, template_name='forum/createPost.html')
