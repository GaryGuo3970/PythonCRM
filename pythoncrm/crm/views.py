from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import path

# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request, "login/login.html")
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username == "admin" and password == "123456":
            return redirect("/crm")
        else:
            error={
                "error":"用户名或密码错误！"
            }
            return render(request, "login/login.html",error)


def crm(request):
    data_string ="test string"
    data_list = ["C#","Java","Go","Python"]
    data_dict = {"key1":"value1","key2":"value2"}
    model={
        "string":data_string,
        "list":data_list,
        "dict":data_dict,
        "int": 123,
    }
    return render(request,"index.html",model)

def customerlist(request):
    data_customers=[
        {
            "no":"C001",
            "name":"Porsche",
            "email":"xxx@xxx.com",
            "phone":"15811112222",
            "address":"上海",
            "age":100
        },
        {
            "no":"C001",
            "name":"Porsche",
            "email":"xxx@xxx.com",
            "phone":"15811112222",
            "address":"上海",
            "age":100
        },
        {
            "no":"C001",
            "name":"Porsche",
            "email":"xxx@xxx.com",
            "phone":"15811112222",
            "address":"上海",
            "age":100
        }
    ]
    model={
        "customers":data_customers
    }
    return render(request,"temp/customerlist.html",model)

def douban(request):
    import requests
    import json

    url = "https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=10"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }   
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.text)
    else:
        data = []

    # 处理数据，提取所需信息
    movies = []
    for item in data:
        movie = {
            "title": item["title"],
            "rank": item["rank"],
            "release_date": item["release_date"],
            "regions": item["regions"],
            "score": item["score"],
            "rating": item["rating"],
            "cover_url": item["cover_url"],
            "url": item["url"]
        }
        movies.append(movie)
    
    # 将数据传递给模板
    model = {
        "movies": movies
    }

    return render(request,"temp/douban.html",model)

def GetStudy(request):
    # 1 请求方法
    print(request.method) 
    # 2 GET请求参数  
    print(request.GET)
    print(request.GET.get("username"))
    # 3 POST请求参数
    print(request.POST)
    # 4 Cookies
    print(request.COOKIES)
    # 5 Sessions
    print(request.session.get("username"))
    # 6 Headers
    print(request.headers)
    # 7 URL参数
    print(request.path)
    # 8 URL反向解析
    print(request.path_info)
    # 9 请求体
    print(request.body)
    # 10 请求协议
    print(request.scheme)
    # 11 请求主机
    print(request.get_host())
    # 12 请求协议版本
    print(request.META.get("SERVER_PROTOCOL"))
    # 13 请求方法
    print(request.method)
    # 14 请求路径
    print(request.path)
    # 15 请求查询字符串
    print(request.META.get("QUERY_STRING"))
    # 16 请求IP地址
    print(request.META.get("REMOTE_ADDR"))
    # 17 请求端口号
    print(request.META.get("SERVER_PORT"))
    # 18 请求语言
    print(request.META.get("HTTP_ACCEPT_LANGUAGE"))
    # 19 请求来源
    print(request.META.get("HTTP_REFERER"))
    # 20 请求协议版本
    print(request.META.get("SERVER_PROTOCOL"))
    # 21 请求用户代理
    print(request.META.get("HTTP_USER_AGENT"))
    # 22 请求来源地址
    print(request.META.get("HTTP_REFERER"))
    return HttpResponse("GetStudy")