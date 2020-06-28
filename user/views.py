from django.shortcuts import render
from django.http import HttpResponse,HttpRequest,HttpResponseBadRequest,JsonResponse
import simplejson,bcrypt
from .models import User
# Create your views here.
"""
注册模块：
1、首先判断用户accont是否存在
2，密码加密，存入数据库，返回用户ID.
3、要求用户重新登陆。
"""

def reg(requests:HttpRequest):
    payload = simplejson.loads(requests.body)
    user = User()
    try:
        account = payload['account'].strip()
        print(account)
        query=User.objects.filter(account=account)
        if query.first():
            return HttpResponseBadRequest('用户已存在')
        user.account = account
        user.name = payload['name'].strip()
        password = payload['passwd'].strip().encode()
        print(password)
        try:
            user.passwd = bcrypt.hashpw(password,bcrypt.gensalt()).decode()
            user.save()
            return JsonResponse({'user_id':user.id})
        except :
            raise
    except :
        return HttpResponseBadRequest('参数错误')


def login(requests:HttpRequest):
    payload = simplejson.loads(requests.body)
    try:
        account = payload['account']
        passwd = payload['passwd']
        user = User.objects.filter(account=account).first()
        if bcrypt.checkpw(passwd.encode(),user.passwd.encode()):
            return JsonResponse({'user_id': 'x'})   #返回信息还需要修改~~~~~
        else:
            return HttpResponseBadRequest('用户名密码错误')
    except Exception as e:
        return HttpResponseBadRequest('参数错误')