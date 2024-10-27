from django import forms

class LoginForm(forms.Form):
    user_id = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User ID'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
