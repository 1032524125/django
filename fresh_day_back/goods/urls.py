from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from goods import views

urlpatterns = [
    #商品分类
    url(r'goods_category_list/',login_required(views.goods_category_list),name='goods_category_list'),
    #进入商品列表
    url(r'^goods_list/',views.goods_list,name='goods_list'),
    #进入商品操作
    url(r'goods_category_detail/(?P<num>\d+)',login_required(views.goods_category_detail)
                                                            ,name='goods_category_detail'),
    #添加商品
    url(r'^goods_detail/',views.goods_detail,name='goods_detail')
]