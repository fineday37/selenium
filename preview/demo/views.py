from django.shortcuts import render
import time


def runoob(request):
    #context = {'hello': "<a href='https://www.runoob.com/'>点击跳转</a>"}
    times = time.strftime("%Y-%m-%d %H-%M:%S", time.localtime())
    current = {'time': times, 'hello': "<a href='https://www.runoob.com/'>点击跳转</a>"}
    return render(request, 'runoob.html', current)
