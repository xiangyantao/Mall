"""myobject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from web.views import index, cart, orders, vip

urlpatterns = [
    # 前台首页
    url(r'^$', index.index, name='index'), # 商城首页
    url(r'^list$', index.lists, name='list'), # 商城列表
    url(r'^list/(?P<pIndex>[0-9]+)$', index.lists, name='list'), # 商品列表
    url(r'^detail/(?P<gid>[0-9]+)$', index.detail, name='detail'), # 商品详情列表

    # 会员登录和退出路由配置
    url(r'^login$', index.login, name='login'),
    url(r'^dologin$', index.dologin, name='dologin'),
    url(r'^logout$', index.logout, name='logout'),

    # 购物车信息管理路由配置
    url(r'^cart$', cart.index, name="cart_index"),
    url(r'^cart/add/(?P<gid>[0-9]+)$', cart.add, name="cart_add"),
    url(r'^cart/del/(?P<gid>[0-9]+)$', cart.delete, name="cart_del"),
    url(r'^cart/clear$', cart.clear, name="cart_clear"),
    url(r'^cart/change$', cart.change, name="cart_change"),

    # 订单处理
    url(r'^orders/add$', orders.add,name='orders_add'), #订单的表单页
    url(r'^orders/confirm$', orders.confirm,name='orders_confirm'), #订单确认页
    url(r'^orders/insert$', orders.insert,name='orders_insert'), #执行订单添加操作

    # 会员中心
    url(r'^vip/orders$', vip.viporders,name='vip_orders'), #会员中心我的订单
    url(r'^vip/odstate$', vip.odstate,name='vip_odstate'), #修改订单状态（确认收货）
    #url(r'^vip/info$', vip.info,name='vip_info'), #会员中心的个人信息
    #url(r'^vip/update$', vip.update,name='vip_update'), #执行修改会员信息
    #url(r'^vip/resetps$', vip.resetps,name='vip_resetps'), #重置密码表单
    #url(r'^vip/doresetps$', vip.doresetps,name='vip_doresetps'), #执行重置密码
]
