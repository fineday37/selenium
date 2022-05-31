from django.shortcuts import render, HttpResponse

from model.models import Test, Contact, Book
import time


# 数据库操作
def testdb(repuest):
    test1 = Test(name='帕克', description="蜘蛛侠")
    test1.save()
    list = Test.objects.values("pk", "name")
    res = list[0]["name"]
    test2 = Book(id=2, title=res, price="88", pub_date="2022-08-09")
    test2.save()
    res2 = Book.objects.filter(pk=2)
    print(res2)
    # # res2 = Test.objects.get(name='luxueqi')
    return HttpResponse("<p>" + res + "</p>")


def Contacts(request):
    test0 = Contact.objects.get(name="楚子航")
    res = test0.email
    print(Contact, type(test0))
    return HttpResponse("<p>" + res + "<p>")