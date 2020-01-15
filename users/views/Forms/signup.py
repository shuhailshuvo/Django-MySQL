from django import forms


class SignUpForm(forms.Form):
    name = forms.CharField(label='Your name')
    email = forms.EmailField(label='Your Email')
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")
