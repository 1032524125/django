from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from django.contrib.auth.hashers import make_password, check_password
from django.urls import reverse
from user.forms import UserRegisterForm, UserSiteForm
from user.models import User, UserAddress
# from utils.functions import is_login
from order.models import OrderGoods, OrderInfo


# Create your views here.


def register(request):
    if request.method == 'GET':
        # 如果请求为GET，返回注册页面
        return render(request, 'register.html')
    if request.method == 'POST':
        # 校验参数
        form = UserRegisterForm(request.POST)
        # 判断is_valid()是否为True
        if form.is_valid():
            # 注册.使用make_password进行密码加密，否则为明文
            password = make_password(form.cleaned_data['password'])
            User.objects.create(username=form.cleaned_data['username'],
                                password=password, email=form.cleaned_data['email'])
            # 跳转到登录页面
            return HttpResponseRedirect(reverse('user:login'))

        else:
            return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        # 使用cookie+session形式实现登录
        username = request.POST.get('username')
        password = request.POST.get('password')
        # all()校验参数，如果为空 返回False
        if not all([username, password]):
            msg = '请填写完整'
            return render(request, 'login.html', {'msg': msg})
        # 校验是否能通过username和password找到user对象
        user = User.objects.filter(username=username).first()
        if user:
            # 校验密码
            if not check_password(password, user.password):
                return render(request, 'login.html')
            else:
                # 设置session值
                request.session['user_id'] = user.id
                return HttpResponseRedirect(reverse('home:index'))
        else:
            msg = '用户名错误'
            return render(request, 'login.html', {'msg': msg})


# @is_login
def logout(request):
    if request.method == 'GET':
        # 注销，删除session和cookie
        request.session.flush()
        # 获取session_key的并实现删除,删除服务端
        session_key = request.session.get('user_id')
        request.session.delete(session_key)

        return HttpResponseRedirect(reverse('user:login'))


def back_register(request):
    if request.method == 'GET':
        return HttpResponseRedirect(reverse('user:register'))


# def cart(request):
#     if request.method == 'GET':
#         return render(request,'cart.html')


def back_login(request):
    if request.method == 'GET':
        return HttpResponseRedirect(reverse('user:login'))


def user_center_info(request):
    if request.method == 'GET':
        # 得到登陆者信息
        user_id = request.session.get('user_id')
        user = UserAddress.objects.filter(user_id=user_id).first()
        return render(request, 'user_center_info.html',{'user':user})


def user_center_order(request):
    if request.method == 'GET':
        # 获取订单数据
        user_id = request.session.get('user_id')
        # 拿到用户
        user = User.objects.filter(pk=user_id).filter().first().username
        # 通过用户拿到订单信息
        order_info_all = OrderInfo.objects.filter(user_id=user_id).all()
        return render(request, 'user_center_order.html', {'order_info': order_info_all})


def user_center_site(request):
    if request.method == 'GET':
        # 从数据库中拿出地址
        user_id = request.session.get('user_id')
        user_address = UserAddress.objects.filter(user_id=user_id).first()
        return render(request, 'user_center_site.html', {'user_address': user_address})

    if request.method == 'POST':
        form = UserSiteForm(request.POST)
        # 检验表单是否填写完整
        if form.is_valid():
            # 填写完整后把信息写入数据库

            signer_name = form.cleaned_data['signer_name']
            address = form.cleaned_data['address']
            signer_postcode = form.cleaned_data['signer_postcode']
            signer_mobile = form.cleaned_data['signer_mobile']
            # 保存信息
            user_id = request.session.get('user_id')
            UserAddress.objects.create(signer_name=signer_name, address=address,
                                       signer_postcode=signer_postcode, signer_mobile=signer_mobile, user_id=user_id)
            return HttpResponseRedirect(reverse('user:user_center_site'))

        else:
            return render(request, 'user_center_site.html', {'form': form})
