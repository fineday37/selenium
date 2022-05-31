from django.http import HttpResponse
from django.shortcuts import render


# 表单
def search_form(request):
    return render(request, 'search_form.html')


# 接收请求数据
def search(request):
    request.encoding = 'utf-8'
    if '原神' in request.GET['q']:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)


def name(request):
    names = request.GET.get("name")
    return HttpResponse("姓名是{}".format(names))
