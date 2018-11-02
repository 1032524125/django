from django.shortcuts import render
from django.contrib import auth

from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from app.forms import UserLoginForm
# Create your views here.


def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    if request.method == 'POST':
        #1.表单验证
        form = UserLoginForm(request.POST)
        #使用is_valid()进行表单验证
        if form.is_valid():
            #form表单验证成功
            user = auth.authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user:
                #如果验证通过，进行登录
                #request.user默认AnonyMouseUser
                auth.login(request,user)
                return HttpResponseRedirect(reverse('app:index'))
            else:
                #用户名和密码错误
                return render(request,'login.html',{'form':form})
        #2.auth模块验证
        #3.auth.login登录
        else:
            #form验证失败，则返回错误信息到页面
            return render(request,'login.html',{'form':form})


def index(request):
    if request.method == 'GET':
        return render(request,'index.html')


def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        return HttpResponseRedirect(reverse('app:login'))





def goods_list(request):
    if request.method == 'GET':
        return render(request,'goods_list.html')


def order_list(request):
    if request.method == 'GET':
        return render(request,'order_list.html')

def user_list(request):
    if request.method == 'GET':
        return render(request,'user_list.html')