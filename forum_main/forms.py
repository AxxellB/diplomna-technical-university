from django import forms

from forum_main.models import Post, Reply, Rule


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'views', 'tag_color', 'category_color', 'created_date')


class CreateReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('text',)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!',
        required=True
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('This field is required!')


class RulesForm(forms.ModelForm):
    class Meta:
        model = Rule
        fields = '__all__'
