from django.shortcuts import render, HttpResponse, redirect
from django.core.exceptions import ValidationError
from django import forms
from model import My_form
from model import models


def ab_form(request):
    # 定义一个字典，用来返回提示信息，如果是get请求，没有，如果是post，添加数据
    back_dic = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 对拿到的数据进行判断
        if '龙族' in username:
            back_dic['username_error'] = '楚子航'
        if len(password) < 3:
            back_dic['password_error'] = '你输入的数据有点短'
    return render(request, 'ab_form.html', locals())


def add_emp(request):
    if request.method == "GET":
        form = My_form.MyForm()  # 初始化form对象
        return render(request, "add_emp.html", {"form": form})
    else:
        form = My_form.MyForm(request.POST)  # 将数据传给form对象
        if form.is_valid():  # 进行校验
            data = form.cleaned_data
            data.pop("r_salary")
            models.Personnel.objects.create(**data)
            return redirect("/index/")
        else:  # 校验失败
            clear_errors = form.errors.get("__all__")  # 获取全局钩子错误信息
            return render(request, "add_emp.html", {"form": form, "clear_errors": clear_errors})
