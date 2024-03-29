# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/11/24 0024 17:30'

from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    """登录表单"""
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)


class RegisterForm(forms.Form):
    """注册验证表单"""
    username = forms.CharField(required=True, min_length=2, max_length=10)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=6, max_length=20)
    password_again = forms.CharField(required=True, min_length=6, max_length=20)
    captcha = CaptchaField(error_messages={"invalid": "验证码输入错误"})  # 验证码，可以自定义错误。key（invalid是固定的），value自己可以随意写
