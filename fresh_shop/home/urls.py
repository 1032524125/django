from django.conf.urls import url
from home import views

urlpatterns = [

    #首页
    url(r'^index/',views.index,name='index'),
    # #进入购物车
    # url(r'^cart',views.cart,name='cart'),
    #返回首页
    url(r'^back_index/',views.back_index,name='back_index'),
    #主页面刷新
    url(r'^flush/',views.flush,name='flush'),



]