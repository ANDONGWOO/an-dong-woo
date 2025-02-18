from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login#로그인
from django.contrib.auth import logout as auth_logout#로그아웃
from django.contrib.auth.decorators import login_required#로그인 할떄
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


# Create your views here.

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("articles:index")
    else:
        form= AuthenticationForm()
    context={
        "form":form,
    }
    return render(request,'accounts/login.html', context)
def logout(request):
    auth_logout(request)
    return redirect("articles:index")
def detail(request,user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    context={
        "user":user
    }
    return render(request,'accounts/detail.html', context)