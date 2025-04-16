import time
from importlib import import_module

from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

class LoginMiddleWare(MiddlewareMixin):
    def __init__(self, get_response):
        super().__init__(get_response)

    def process_request(self, request):
        print("测试中间件：请求", request)            
        request.session_username=""        
        user_info = request.session.get("user_info")
        if user_info:
            request.session_userid=user_info.get("username")
            request.session_username=user_info.get("username")
            return        
        
        if request.path_info in {"/login","/"}:
            return
        
        return redirect("/login")
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        print("测试中间件：视图", view_func, view_args, view_kwargs)
        # 1 .获取当前请求的url
        # 2 .获取当前请求的视图函数
        # 3 .获取当前用户的权限
        # 4 .获取当前用户的角色
        # 5 .检查当前用户的权限是否有访问该视图函数的权限
        # 6 .如果没有权限，返回403错误
        # 7 .如果有权限，返回None，继续执行视图函数
        # 8 .如果没有登录，返回登录页面
        return None

    def process_response(self, request, response):
        print("测试中间件：相应", response)
        return response
