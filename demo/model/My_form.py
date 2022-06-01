from django import forms
from django.core.exceptions import ValidationError


class EmpForm(forms.Form):
    username = forms.CharField(min_length=3, label="用户名")
    pwd = forms.CharField(min_length=6, label="密码")

