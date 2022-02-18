from django import forms

class login(forms.Form):
    usr = forms.CharField(max_length = 50)
    pswrd = forms.CharField(max_length = 20, widget=forms.PasswordInput())