from django.urls import path

from forum_main.views import forum_view, create_thread, my_threads, edit_thread, delete_thread, thread_details, \
    contacts, rules, add_rule, edit_rule, delete_rule, forum_view_most_popular

urlpatterns = [
    path('', forum_view, name='index'),
    path('create/', create_thread, name='create thread'),
    path('my_threads/', my_threads, name='my threads'),
    path('edit/<int:pk>/', edit_thread, name='edit thread'),
    path('delete/<int:pk>/', delete_thread, name='delete thread'),
    path('details/<int:pk>', thread_details, name='thread details'),
    path('contacts', contacts, name='contacts'),
    path('rules', rules, name='forum rules'),
    path('add_rule/', add_rule, name='add rule'),
    path('edit_rule/<int:pk>', edit_rule, name='edit rule'),
    path('delete_rule/<int:pk>', delete_rule, name='delete rule'),
    path('sort_by_popularity/', forum_view_most_popular, name='sort by most popular')
]