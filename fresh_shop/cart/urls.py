from django.conf.urls import url
from cart import views

urlpatterns = [
    # 添加到购物车
    url(r'^add_cart',views.add_cart,name='add_cart'),
    # 进入购物车
    url(r'^into_cart/',views.into_cart,name='into_cart'),
    # 刷新价格
    url(r'^f_price/',views.f_price,name='f_price')

]