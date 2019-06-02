from django.shortcuts import render
from django.http import HttpResponse


# 前台首页
def index(request):
    '''项目前台首页'''
    return render(request, 'web/index.html')


def list(request,pIndex=1):
    '''商品列表页'''
    return render(request, 'web/list.html')


def detail(request,gid):
    '''商品详情页'''
    return render(request, 'web/detail.html')


