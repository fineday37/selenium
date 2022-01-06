from django.shortcuts import render


def runoob(request):
    context = {'hello': "<a href='https://www.runoob.com/'>点击跳转</a>"}
    return render(request, 'runoob.html', context)
