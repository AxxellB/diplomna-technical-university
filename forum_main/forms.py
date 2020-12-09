from django import forms

from forum_main.models import Post, Reply


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'views', 'tag_color', 'category_color',)


class CreateReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('text',)
