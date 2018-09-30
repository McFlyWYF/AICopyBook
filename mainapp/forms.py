from django.forms import Form,ModelForm
from django import forms


#注册表单
class RegisterForm(forms.Form):

    UserName = forms.CharField(max_length=100)
    UserPassword1 = forms.CharField(max_length=100)
    UserPassword2 = forms.CharField(max_length=100)
    age = forms.CharField(max_length=50)



#登录表单
class LoginForm(forms.Form):

    UserName = forms.CharField(max_length=100)
    UserPassword = forms.CharField(max_length=100)
