from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def setcookie(request):
    # 创建响应对象
    response = HttpResponse()
    # 将数据存储在cookie中
    # 默认有效时间 保存浏览器缓存中 关闭浏览器数据丢失,max_age方法可更改有效时间，单位为秒。24 * 60 * 60代表24小时乘60分乘60秒
    response.set_cookie('uname', 'zhangsan', max_age=24 * 60 * 60)
    return response


def getcookie(request):
    str = request.COOKIES.get('uname')
    return HttpResponse(str)
