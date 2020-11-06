from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def setcookie(request):
    # 创建响应对象
    response = HttpResponse()
    # 将数据存储在cookie中
    response.set_cookie('uname', 'zhangsan')
    return response
