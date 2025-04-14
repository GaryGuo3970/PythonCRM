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

    def process_response(self, request, response):
        print("测试中间件：相应", response)
        return response
