from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from goods.models import Goods
from user.models import User
from cart.models import ShoppingCart


def add_cart(request):
    if request.method == 'POST':
        # 添加到session中的数据格式为:
        # key==>goods,
        # value==>[[id1, num,1], [id2, num,1], [id3, num,0]....]

        # 1.1 添加到购物车的数据，其实就是添加到session中
        # 1.2 如果商品已经加入到session中，则修改session中商品的个数
        # 1.3 如果商品没有添加到session中，则添加

        # 获取从ajax中传递的商品的id和商品的个数
        goods_id = request.POST.get('goods_id')
        goods_num = request.POST.get('goods_num')
        # 组装存储的数据结构
        goods_list = [goods_id, goods_num,1]
        # 判断在session中是否存储了商品信息
        if request.session.get('goods'):
            # 标识符: 用于判断当前加入到购物车的商品
            # 如果购物车中已经存在了该商品，则修改flag为1，否则flag还是为0
            flag = 0
            # 说明购物车中已经存储了商品信息
            session_goods = request.session['goods']
            for goods in session_goods:
                # 循环判断，判断加入到session中的商品是否已经存在于session中
                if goods_id == goods[0]:
                    goods[1] = int(goods[1]) + int(goods_num)
                    # 标识符，修改session中的商品后，标识符修改为1
                    flag = 1
            # flag为0，表示添加到session中的商品之前并没有添加
            if not flag:
                session_goods.append(goods_list)
            # 修改成功session中商品的信息
            request.session['goods'] = session_goods
            cart_count = len(session_goods)
        else:
            # 说明购物车中还没有存储商品信息
            data = []
            data.append(goods_list)
            request.session['goods'] = data
            cart_count = 1

        return JsonResponse({'code': 200, 'cart_count': cart_count})


def into_cart(request):
    if request.method == 'GET':
        # 获取session中的商品对象
        # 判断是否登录
        user_id = request.session.get('user_id')
        if user_id:
            # 登录了则从数据库中拿取数据和session中拿取数据
            shop_cart = ShoppingCart.objects.filter(user_id=user_id)
            goods_all = [(cart.goods,cart.is_select,cart.nums) for cart in shop_cart]
            return render(request,'cart.html',{'goods_all':goods_all})
        else:
            # 没有登录，直接从session中获取值
            # goods = []
            # goods1 = request.session.get('goods')
            # for key in goods1:
            #     id = key[0]
            #
            #     good = Goods.objects.filter(pk=id).first()
            #     goods.append
            session_ids = request.session.get('goods')
            if session_ids:

                goods_all = [(Goods.objects.filter(pk=goods[0]).first(),goods[2],goods[1])for goods in session_ids]
            else:
                goods_all = ''
            return render(request,'cart.html',{'goods_all':goods_all})


def f_price(request):
    if request.method == 'GET':
        # 返回购物车中商品的价格和总价
        # {{key:[id1,price1},...}
        user_id = request.session.get('user_id')
        if user_id:
            # 获取当前登录系统的用户购物车中的数据
            carts = ShoppingCart.objects.filter(user_id=user_id)
            cart_data = {}
            cart_data['goods_price'] = [(cart.goods_id,cart.nums*cart.goods.shop_price)for cart in carts]
            all_price = 0
            for cart in carts:
                if cart.is_select:
                    all_price += cart.nums * cart.goods.shop_price
                    cart_data['all_price'] = all_price
        else:
            session_goods = request.session.get('goods')
            cart_data = {}
            data_all = []
            all_price = 0
            for goods in session_goods:

                data =[]
                data.append(goods[0])
                g = Goods.objects.get(pk=goods[0])
                data.append(int(goods[1])*g.shop_price)
                data_all.append(data)
                # 判断商品勾选后才计算总价格
                if goods[2]:
                    all_price += int(goods[1])*g.shop_price
            cart_data['goods_price'] = data_all
            cart_data['all_price'] = all_price
        return JsonResponse({'code':200, 'cart_data': cart_data})
