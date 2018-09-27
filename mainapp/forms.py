from django.forms import Form,ModelForm,CharField
from django.contrib.auth.hashers import check_password
from .models import MyUser


#注册表单
class RegisterForm(ModelForm):
    class Meta:
        model = MyUser
        fields = ['UserName','UserPassword','UserAge']


#登录表单
class LoginForm(Form):
    UserName = CharField(max_length=100)
    UserPassword = CharField(max_length=100)

    def chk_password(self):
        UserName = self.cleaned_data['UserName']
        UserPassword = self.cleaned_data['UserPassword']

        try:
            user = MyUser.objects.get(UserName=UserName)
            return user,check_password(UserPassword,user.UserPassword)

        except:
            return None,False

