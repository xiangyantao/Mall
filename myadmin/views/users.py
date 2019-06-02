from django.shortcuts import render
from django.http import HttpResponse

from common.models import Users
from datetime import datetime
from django.core.paginator import Paginator


# 浏览会员
def index(request, pIndex):
    
    mod = Users.objects
    mywhere = []
    kw = request.GET.get('keyword', None)
    sexid = request.GET.get('sexid', None)
    list = mod.filter().order_by("username")


    if kw:
        list = list.filter(username__contains=kw)
        mywhere.append('keyword='+kw)


    if sexid:
        list = list.filter(sex=sexid)
        mywhere.append('sexid='+sexid)


    pIndex = int(pIndex)
    page = Paginator(list, 5)
    maxpages = page.num_pages

    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1


    list2 = page.page(pIndex)
    plist = page.page_range

    context ={
        'userslist': list2,
        'plist': plist,
        'pIndex': pIndex,
        'maxpages': maxpages,
        'mywhere': mywhere
    }


    return render(request, 'myadmin/users/index.html', context)

# 会员信息添加表单
def add(request):
    return render(request, 'myadmin/users/add.html')


# 执行会员信息添加
def insert(request):
    try:
        ob = Users()
        ob.username = request.POST['username']
        ob.name = request.POST['name']
        #获取密码并md5
        import hashlib
        m = hashlib.md5() 
        m.update(bytes(request.POST['password'], encoding="utf8"))
        ob.password = m.hexdigest()
        ob.sex = request.POST['sex']
        ob.address = request.POST['address']
        ob.code = request.POST['code']
        ob.phone = request.POST['phone']
        ob.email = request.POST['email']
        ob.state = 1
        ob.addtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': '添加成功！'}
    except Exception as err:
        print(err)
        context = {'info': '添加失败！'}

    return render(request,"myadmin/info.html", context)


# 执行会员信息删除
def delete(request, uid):
    try:
        ob = Users.objects.get(id=uid)
        ob.delete()
        context = {'info': '删除成功！'}
    except:
        context = {'info': '删除失败！'}
    return render(request, "myadmin/info.html", context)


# 打开会员信息编辑表单
def edit(request, uid):
    try:
        ob = Users.objects.get(id=uid)
        context = {'user': ob}
        return render(request, "myadmin/users/edit.html", context)
    except Exception as err:
        print(err)
        context = {'info': '没有找到要修改的信息！'}
    return render(request, "myadmin/info.html", context)


# 执行会员信息编辑
def update(request, uid):
    try:
        ob = Users.objects.get(id=uid)
        ob.name = request.POST['name']
        ob.sex = request.POST['sex']
        ob.address = request.POST['address']
        ob.code = request.POST['code']
        ob.phone = request.POST['phone']
        ob.email = request.POST['email']
        ob.state = request.POST['state']
        ob.save()
        context = {'info': '修改成功！'}
    except Exception as err:
        print(err)
        context = {'info': '修改失败！'}
    return render(request, "myadmin/info.html", context)


def pwupdate(request, uid):
    ob = Users.objects.get(id=uid)
    context = {'user': ob}
    return render(request, "myadmin/users/pwupdate.html", context)


def resetpw(request, uid):
    try:
        ob = Users.objects.get(id=uid)
        if request.POST['newpw'] == request.POST['renewpw']:
            import hashlib
            m = hashlib.md5()
            m.update(bytes(request.POST['newpw'], encoding="utf8"))
            ob.password = m.hexdigest()
            ob.save()
            context = {'info': '修改成功！'}
    except Exception as err:
        print(err)
        context = {'info': '修改失败！'}
    return render(request, "myadmin/info.html", context)

