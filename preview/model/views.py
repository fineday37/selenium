from django.shortcuts import render, HttpResponse
from .My_form import EmpForm
from django.core.exceptions import ValidationError


def add_emp(request):
    if request.method == "GET":
        form_obj = EmpForm()
        return render(request, "add_emp.html", {"form": form_obj})
    else:
        form_obj = EmpForm(request.POST)
        if form_obj.is_valid():
            username = form_obj.cleaned_data.get("username")
            pwd = form_obj.cleaned_data.get("pwd")
            if username == "楚子航" and pwd == "永燃的瞳术师":
                return HttpResponse('ok')
        else:
            clean_errors = "错误"

            return render(request, "add_emp.html", {"form_obj": form_obj, "clean_errors": clean_errors})
