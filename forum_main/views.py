from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
from forum_main.color_maps import tag_color_map, category_color_map
from forum_main.forms import CreatePostForm, CreateReplyForm
from forum_main.models import Post, Reply


def forum_view(request):
    query = request.GET.get('q', "")
    if query != "":
        posts = get_forum_queryset(query)
    else:
        posts = Post.objects.all()

    paginator = Paginator(posts, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'query': str(query),
        'page_obj': page_obj
    }
    return render(request, 'forum/forum.html', context)


@login_required
def create_thread(request):
    if request.method == 'GET':
        context = {
            'form': CreatePostForm
        }

    else:
        form = CreatePostForm(request.POST)
        if form.is_valid():
            tag_color = tag_color_map[form.cleaned_data['tag']]
            category_color = category_color_map[form.cleaned_data['category']]
            form = form.save(commit=False)
            form.tag_color = tag_color
            form.category_color = category_color
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


def edit_thread(request, pk):
    current_post = Post.objects.get(pk=pk)
    if request.method == 'GET':
        form = CreatePostForm(instance=current_post)
        context = {
            'form': form,
            'pk': pk
        }
    else:
        form = CreatePostForm(request.POST, instance=current_post)
        if form.is_valid():
            form.save()
            return redirect('my threads')
        context = {
            'form': form,
            'pk': pk
        }

    return render(request, context=context, template_name='forum/edit_thread.html')


def delete_thread(request, pk):
    current_post = Post.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'pk': pk
        }
        return render(request, context=context, template_name='forum/delete_thread.html')
    else:
        current_post.delete()
        return redirect('my threads')


def thread_details(request, pk):
    current_thread = Post.objects.get(pk=pk)
    replies = Reply.objects.filter(post=current_thread)
    comments_count = len(replies)
    context = {}

    if request.method == 'GET':
        current_thread.views += 1
        current_thread.save()

    else:
        form = CreateReplyForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.post = current_thread
            form.save()
            current_thread.replies += 1
            current_thread.save()
            return redirect('thread details', pk)

    context = {
        'pk': pk,
        'post': current_thread,
        'replies': replies,
        'comments_count': comments_count,
    }
    return render(request, context=context, template_name='forum/thread_details.html')


def get_forum_queryset(query=None):
    filtered_posts = []
    queries = query.split(" ")
    for q in queries:
        posts = Post.objects.filter(
            Q(name__icontains=q) |
            Q(description__icontains=q)
        ).distinct()

        for post in posts:
            filtered_posts.append(post)

    return list(set(filtered_posts))





