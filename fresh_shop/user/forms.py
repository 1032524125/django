from django import forms

from user.models import User


class UserRegisterForm(forms.Form):
    username = forms.CharField(required=True,max_length=20,
                               error_messages={'required':'用户名必填'})
    password = forms.CharField(required=True,min_length=8,max_length=20,
                               error_messages={'required':'密码必填'})
    password2 = forms.CharField(required=True,min_length=8,max_length=20,
                                error_messages={'required':'密码必填'})
    email = forms.EmailField(required=True,
                             error_messages={'required':'邮箱必填'})

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        # 检验用户名是否被注册过
        user = User.objects.filter(username=username)
        if user:
            raise forms.ValidationError({'username':'用户名已存在'})
        if password != password2:
            raise forms.ValidationError({'password2':'两次密码不一致'})


class UserLoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=20,
                               error_messages={'required': '用户名必填'})
    password = forms.CharField(required=True, min_length=8, max_length=20,
                               error_messages={'required': '密码必填'})

    def clean(self):
        # 验证用户名是否注册过
        user = User.objects.filter(username=self.username).first()
        if not user:
            raise forms.ValidationError({'username':'用户名没有注册'})
        else:
            return self.cleaned_data


class UserSiteForm(forms.Form):
    signer_name = forms.CharField(required=True,max_length=20,
                                  error_messages={'required':'用户名必填'})
    address = forms.CharField(required=True,max_length=100,
                              error_messages={'required': '用户名必填'})
    signer_postcode = forms.CharField(required=True,max_length=11,
                                      error_messages={'required': '用户名必填'})
    signer_mobile = forms.CharField(required=True,max_length=11,
                                   error_messages={'required': '用户名必填'})
