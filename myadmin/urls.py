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
from django.urls import path, re_path, include
from myadmin.views import index, users, type, goods

urlpatterns = [
    # 后台首页
    path('', index.index, name="myadmin_index"),

    # 后台用户管理
    path('users/<int:pIndex>', users.index, name="myadmin_users_index"),
    path('users/add', users.add, name="myadmin_users_add"),
    path('users/insert', users.insert, name="myadmin_users_insert"),
    path('users/del/<int:uid>', users.delete, name="myadmin_users_del"),
    path('users/edit/<int:uid>', users.edit, name="myadmin_users_edit"),
    path('users/update/<int:uid>', users.update, name="myadmin_users_update"),
    path('users/pwupdate/<int:uid>', users.pwupdate, name="myadmin_users_pwupdate"),
    path('users/resetpw/<int:uid>', users.resetpw, name="myadmin_users_resetpw"),

    # 后台管理员路由
    path('login', index.login, name='myadmin_login'),
    path('dologin', index.dologin, name='myadmin_dologin'),
    path('logout', index.logout, name='myadmin_logout'),
    path('verify', index.verify, name='myadmin_verify'), # 验证码

    # 后台商品类别信息管理
    path('type', type.index, name='myadmin_type_index'),
    path('type/add/<int:tid>', type.add, name='myadmin_type_add'),
    path('type/insert', type.insert, name="myadmin_type_insert"),
    path('type/del/<int:tid>', type.delete, name="myadmin_type_del"),
    path('type/edit/<int:tid>', type.edit, name="myadmin_type_edit"),
    path('type/update/<int:tid>', type.update, name="myadmin_type_update"),

    # 后台商品信息管理
    path('goods/<int:pIndex>', goods.index, name="myadmin_goods_index"),
    path('goods/add', goods.add, name="myadmin_goods_add"),
    path('goods/insert', goods.insert, name="myadmin_goods_insert"),
    path('goods/del/<int:gid>', goods.delete, name="myadmin_goods_del"),
    path('goods/edit/<int:gid>', goods.edit, name="myadmin_goods_edit"),
    path('goods/update/<int:gid>', goods.update, name="myadmin_goods_update"),
]
