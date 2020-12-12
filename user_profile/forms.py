from django import forms


class ChangeEmailForm(forms.Form):
    error_messages = {
        'email_mismatch': 'The two email addresses fields did not match.',
        'not_changed': 'The email address is the same as the one already defined.',
        'password_incorrect': 'The password you entered is incorrect.'
    }
    password = forms.CharField(
        widget=forms.PasswordInput()
    )
    new_email1 = forms.EmailField(
        label='New Email',
        widget=forms.EmailInput()
    )
    new_email2 = forms.EmailField(
        label='Confirm New Email',
        widget=forms.EmailInput()
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(ChangeEmailForm, self).__init__(*args, **kwargs)

    def clean_password(self):
        """
        Validate that the password field is correct.
        """
        password = self.cleaned_data["password"]
        if not self.user.check_password(password):
            raise forms.ValidationError(
                self.error_messages['password_incorrect'],
                code='password_incorrect',
            )
        return password

    def clean_new_email1(self):
        old_email = self.user.email
        new_email1 = self.cleaned_data.get('new_email1')
        if new_email1 and old_email:
            if new_email1 == old_email:
                raise forms.ValidationError(
                    self.error_messages['not_changed'],
                    code='not_changed',
                )
        return new_email1

    def clean_new_email2(self):
        new_email1 = self.cleaned_data.get('new_email1')
        new_email2 = self.cleaned_data.get('new_email2')
        if new_email1 and new_email2:
            if new_email1 != new_email2:
                raise forms.ValidationError(
                    self.error_messages['email_mismatch'],
                    code='email_mismatch',
                )
        return new_email2

    def save(self, commit=True):
        email = self.cleaned_data["new_email1"]
        self.user.email = email
        if commit:
            self.user.save()
        return self.user
