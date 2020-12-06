from django import forms

from forum_main.models import Post


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
