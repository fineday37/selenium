# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# 接收POST请求数据
@csrf_exempt
def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)
