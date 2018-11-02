from django.conf.urls import url
from user import views

urlpatterns = [
#注册
    url(r'register/',views.register,name='rsgister'),
    #回到注册页面
    url(r'^back_register/',views.back_register,name='back_register'),
    #登录
    url(r'^login/',views.login,name='login'),
    #进入登录页面
    url(r'^back_login/',views.back_login,name='back_login'),
    #注销
    url(r'logout/',views.logout,name='logout'),
    # 进入用户中心
    url(r'^user_center_info/',views.user_center_info,name='user_center_info'),
    # 进入全部订单
    url(r'^user_center_order/',views.user_center_order,name='user_center_order'),
    # 地址
    url('^user_center_site/',views.user_center_site,name='user_center_site'),
    ]
