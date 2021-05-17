from django import forms

from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)
    
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not "gmail.com" in email:
            raise forms.ValidationError("Not correct email")
        return email


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=50, label="Confirm password", widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("This username is already taken")
        return username



    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        confirmed_password = self.cleaned_data.get('confirm_password')
        if confirmed_password != password:
            raise forms.ValidationError("Passwords didn't match")
        return data