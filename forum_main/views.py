from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
from forum_main.color_maps import tag_color_map, category_color_map
from forum_main.forms import CreatePostForm, CreateReplyForm, ContactForm, RulesForm
from forum_main.models import Post, Reply, Rule, Category, Tag

def is_superuser(user):
    return user.is_superuser

def forum_view(request):
    query = request.GET.get('q', '')
    sort_by = request.GET.get('sort', 'newest')

    if query != " ":
        posts = get_forum_queryset(query)
    elif sort_by == "newest":
        posts = Post.objects.all().order_by('-created_date')
    else:
        posts = Post.objects.all().order_by('-replies', '-views')

    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'query': str(query),
        'page_obj': page_obj,
        'sort_by': sort_by,
        'is_superuser': request.user.is_superuser
    }

    return render(request, 'forum/forum.html', context)



@login_required(login_url='login user')
def create_thread(request):
    if request.method == 'GET':
        context = {
            'form': CreatePostForm
        }

    else:
        form = CreatePostForm(request.POST)
        if form.is_valid():
            form.category = form.cleaned_data['category']
            form.tag = form.cleaned_data['tag']
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('index')
        context = {
            'form': form
        }

    return render(request, context=context, template_name='forum/create_thread.html')


@login_required(login_url='login user')
def my_threads(request):
    if request.method == 'GET':
        user = request.user
        my_posts = Post.objects.filter(user=user).order_by('-created_date')
        paginator = Paginator(my_posts, 4)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        show_buttons = True
        context = {
            'posts': page_obj,
            'show_buttons': show_buttons
        }
        return render(request, context=context, template_name='forum/my_threads.html')

@login_required(login_url='login user')
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

@login_required(login_url='login user')
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

@login_required(login_url='login user')
@user_passes_test(is_superuser)
def edit_thread_superuser(request, pk):
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
            return redirect('index')
        context = {
            'form': form,
            'pk': pk
        }

    return render(request, context=context, template_name='forum/edit_thread_superuser.html')

@login_required(login_url='login user')
@user_passes_test(is_superuser)
def delete_thread_superuser(request, pk):
    current_post = Post.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'pk': pk
        }
        return render(request, context=context, template_name='forum/delete_thread_superuser.html')
    else:
        current_post.delete()
        return redirect('index')

def thread_details(request, pk):
    current_thread = Post.objects.get(pk=pk)
    replies = Reply.objects.filter(post=current_thread).order_by('-id')
    comments_count = len(replies)

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
    if queries:
        for q in queries:
            filtered_posts = Post.objects.filter(
                Q(name__icontains=q) |
                Q(description__icontains=q)
            )

        return filtered_posts


def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            client_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            from_email = 'axxellblaze@gmail.com'
            content = EmailMessage(
                subject=subject,
                body=message,
                from_email=from_email,
                to=[from_email],
                reply_to=[client_email],
            )
            try:
                content.send()
                messages.success(request, 'Your email was sent successfully!')
                return redirect('contacts')
            except:
                messages.error(request, 'Your email could not be sent! Please contact'
                                            ' an administrator if this issue continues!')
        return render(request, "common_site_pages/contact.html", {'form': form})
    else:
        context = {
            'form': ContactForm()
        }
    return render(request, 'common_site_pages/contact.html', context)


def rules(request):
    if request.method == 'GET':
        rules = Rule.objects.all().order_by('id')
        return render(request, 'common_site_pages/forum_rules.html', {'rules': rules})

@user_passes_test(is_superuser)
def add_rule(request):
    if request.method == 'GET':
        context = {
            'form': RulesForm
        }
    else:
        form = RulesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forum rules')
        context = {
            'form': form
        }
    return render(request, 'common_site_pages/create_rule.html', context)

@user_passes_test(is_superuser)
def edit_rule(request, pk):
    current_rule = Rule.objects.get(pk=pk)
    if request.method == 'GET':
        form = RulesForm(instance=current_rule)
        context = {
            'form': form,
            'pk': pk
        }
    else:
        form = RulesForm(request.POST, instance=current_rule)
        if form.is_valid():
            form.save()
            return redirect('forum rules')
        context = {
            'form': form,
            'pk': pk
        }

    return render(request, 'common_site_pages/edit_rule.html', context)

@user_passes_test(is_superuser)
def delete_rule(request, pk):
    current_rule = Rule.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'pk': pk
        }
        return render(request, context=context, template_name='common_site_pages/delete_rule.html')
    else:
        current_rule.delete()
        return redirect('forum rules')







