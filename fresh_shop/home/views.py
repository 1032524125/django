from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse
# Create your views here.
from goods.models import Goods, GoodsCategory
from django.urls import reverse
# from utils.functions import is_login
from user.models import User


def index(request):
    if request.method == 'GET':
        '''获取对象'''
        # 获取商品分类
        category_types = GoodsCategory.CATEGORY_TYPE
        # 获取商品，按照降序排列
        goods = Goods.objects.all().order_by('-id')

        data_all = {}
        for type in category_types:
            data = []
            count = 0
            for good in goods:
                if count < 4:
                    if type[0] == good.category.category_type:
                        data.append(good)
                        count +=1

            data_all['goods_' + str(type[0])] = data
        return render(request,'index.html',{'data_all':data_all,'category_types':category_types})


def back_index(request):
    if request.method == 'GET':
        return HttpResponseRedirect(reverse('home:index'))


def flush(request):
    if request.method == 'GET':
        # 获取登陆后的用户名
        user_id = request.session.get('user_id')
        if user_id:
            user = User.objects.filter(pk=user_id).first()
            return JsonResponse({'code': 200, 'user': user})

        else:
            pass


