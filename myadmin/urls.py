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
from django.conf.urls import url, include
from myadmin.views import index,users

urlpatterns = [
    # 后台首页
    # path('', index.index, name='myadmin_index'),
    url(r'^$', index.index, name="myadmin_index"),


    # 后台用户管理
    # path('users/', user.index, name="myadmin_users_index"),
    # path('users/add',users.add, name="myadmin_users_add"),
    # path('users/insert',users.insert, name="myadmin_users_insert"),
    # path('users/del')
    url(r'^users$', users.index, name="myadmin_users_index"),
    url(r'^users/add$', users.add, name="myadmin_users_add"),
    url(r'^users/insert$', users.insert, name="myadmin_users_insert"),
    url(r'^users/del/(?P<uid>[0-9]+)$', users.delete, name="myadmin_users_del"),
    url(r'^users/edit/(?P<uid>[0-9]+)$', users.edit, name="myadmin_users_edit"),
    url(r'^users/update/(?P<uid>[0-9]+)$', users.update, name="myadmin_users_update"),

    # 后台管理员路由
    url(r'^login$', index.login, name='myadmin_login'),
    url(r'^dologin$', index.dologin, name='myadmin_dologin'),
    url(r'^logout$', index.logout, name='myadmin_logout'),
    url(r'^verify$', index.verify, name='myadmin_verify'), # 验证码

]

