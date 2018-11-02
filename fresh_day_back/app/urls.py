from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from app import views
urlpatterns = [
    #登录界面
    url(r'^login/',views.login,name='login'),
    #主页面
    url(r'^index/',login_required(views.index),name='index'),
    #注销
    url(r'^logout/',views.logout,name='logout'),


    #进入订单列表
    url(r'^order_list/',views.order_list,name='order_list'),
    #进入用户列表
    url(r'^user_list/',views.user_list,name='user_list')

]