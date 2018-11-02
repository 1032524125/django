from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from goods.models import GoodsCategory
from goods.forms import GoodsDetailForm


def goods_category_list(request):
    if request.method == 'GET':
        #获取分类信息
        categorys = GoodsCategory.objects.all()
        categorys_types = GoodsCategory.CATEGORY_TYPE
        return render(request, 'goods_category_list.html',{'categorys': categorys,
                                                             'categorys_types':categorys_types})


def goods_category_detail(request,num):
    if request.method == 'GET':
        category = GoodsCategory.objects.get(pk=num)
        categorys_types = GoodsCategory.CATEGORY_TYPE
        return render(request,'goods_category_detail.html',{'category':category,
                                                            'categorys_types': categorys_types})

    if request.method == 'POST':
        #获取图片
        category_front_image = request.FILES.get('category_front_image')
        if category_front_image:
            category = GoodsCategory.objects.get(pk=num)
            category.category_front_image= category_front_image
            #保存
            category.save()
        return HttpResponseRedirect(reverse('goods:goods_category_list'))



def goods_list(request):
    if request.method == 'GET':
        #获取对象
        categorys = GoodsCategory.objects.all()
        categorys_types = GoodsCategory.CATEGORY_TYPE
        return render(request,'goods_list.html',{'categorys':categorys,
                                                     'categorys_types': categorys_types})


def goods_detail(request):
    if request.method == 'GET':
        return render(request,'goods_detail.html')
    if request.method == 'POST':
        #表单验证
        form = GoodsDetailForm(request.POST)
        if form.is_valid():
            #
            pass
        else:
            return render(request,'goods_detail.html')
