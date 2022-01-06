from django.http import HttpResponse

from model.models import Test


# 数据库操作
def testdb(request):
    test1 = Test(name='飞蓬',description="仙剑")
    test1.save()
    global res
    list = Test.objects.all()
    # res2 = Test.objects.get(name='luxueqi')
    for var in list:
        res = var.name + ''
    return HttpResponse("<p>" + res + "</p>")