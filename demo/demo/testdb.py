from django.shortcuts import render, HttpResponse

from model.models import Test, Contact, Book, Emp
import time


# 数据库操作
def testdb(repuest):
    name = "楚子航"
    test1 = Test(name=name, description="软子哥")
    test1.save()
    horizon = Test.objects.filter(name=name).first()
    horizon_id = horizon.pk
    list = Test.objects.values("pk", "name")
    res = list[horizon_id-1]["name"]
    list2 = Test.objects.filter(name='荆州').first()
    book = Book.objects.create(title=res, price=738, pub_date='2022-09-08', test_id=horizon)
    # test2 = Book(id=2, title=res, price="88", pub_date="2022-08-09")
    # test2.save()
    test3 = Book.objects.filter(pk=2).first()
    res2 = test3.title
    # res2 = Test.objects.get(name='luxueqi')
    return HttpResponse("<p>" + "新增" + "</p>")


def Contacts(request):
    test0 = Emp.objects.filter(pk=1).first()
    test1 = test0.name
    book = Book.objects.filter(pk=5).first()
    books = book.title
    book.authors.add(test0)
    return HttpResponse("<p>" + books + " " + test1 + "<p>")
