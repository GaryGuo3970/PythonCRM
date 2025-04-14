from functools import wraps
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls import path
from crm.models import Admin, Customer, Dealer, Dealer_Type,Department

# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request, "login/login.html")
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if Admin.objects.filter(username=username, password=password).exists():
            request.session["user_info"]={
                "username":username,
                "password":password
            }
            return redirect("/")
        else:
            error={
                "error":"用户名或密码错误！"
            }
            return render(request, "login/login.html",error)
        
def logout(request):
    request.session.flush()  # 清除session
    return redirect("/")
        
def login_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.session.get("user_info"):
            return view_func(request, *args, **kwargs)
        else:
            return redirect("/login")
    return _wrapped_view

def crm(request):
    return render(request,"index.html")

def dealerTypelist(request):   
    model= {"dealer_types":Dealer_Type.objects.all().values()}
    for m in model:
        print(m)
    return render(request,"basicdata/dealer_type_list.html",model)

def dealerTypeAdd(request):
    if request.method == "GET":
        return render(request,"basicdata/dealer_type_add.html")
    
    if request.method == "POST":
        dealer_type = Dealer_Type()
        dealer_type.no = request.POST.get("no")
        dealer_type.name = request.POST.get("name")
        dealer_type.description = request.POST.get("description")
        dealer_type.category = request.POST.get("category")
        dealer_type.save()
        return redirect("/crm/dealertype")
    
def dealerTypeDelete(request):
    if request.method == "GET":
        id = request.GET.get("id")
        if(id):
            dealer_type = Dealer_Type.objects.filter(id=id).first()
            model = {
                "model":dealer_type
            }
            return render(request,"basicdata/dealer_type_delete.html",model)
        
    
    if request.method == "POST":
        id = request.POST.get("id")
        print(request.POST)
        print(id)
        print("post delete")
        if(id):        
            dealer_type = Dealer_Type.objects.filter(id=id)
            dealer_type.delete() 
        return redirect("/crm/dealertype")

def dealerTypeEdit(request):
    if request.method == "GET":
        id = request.GET.get("id")
        if(id):
            dealer_type = Dealer_Type.objects.filter(id=id).first()
            model = {
                "model":dealer_type
            }
            return render(request,"basicdata/dealer_type_edit.html",model)
        
    if request.method == "POST":
        id = request.POST.get("id")
        dealer_type = Dealer_Type.objects.filter(id=id).first()
        dealer_type.no = request.POST.get("no")
        dealer_type.name = request.POST.get("name")
        dealer_type.description = request.POST.get("description")
        dealer_type.category = request.POST.get("category")
        dealer_type.save()
    
    return redirect("/crm/dealertype")

def dealerTypeDetail(request, id):
    pass

def dealerlist(request):
    model=Dealer.objects.all().values()   
    for m in model:
        print(m)
    return render(request,"basicdata/dealer_list.html",{"dealers":model})

def departmentlist(request):
    model=Department.objects.all().values
    return render(request,"basicdata/department_list.html",{"department":model})   

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

def dbOperate(request):
    # 1 新增数据
    if(request.GET.get("add")):
        customer = Customer()

        #customer.no = "C0001"
        customer.address="Shanghai"
        customer.phone="15811112222"
        customer.age=100
        customer.first_name="Gary"
        customer.last_name="Guo"
        customer.is_active=True

        customer.save()

        return HttpResponse("add")

    if(request.GET.get("delete")):        
        customerToDelete = Customer.objects.filter(first_name="Gary")
        allCustomers = Customer.objects.all()
        customerToDelete.delete()
        return HttpResponse("delete")

    if(request.GET.get("update")):    
        customerToDelete = Customer.objects.filter(first_name="Gary")
        customerToDelete.update(age=101)    
        return HttpResponse("update")
    
    if (request.GET.get("select")):    
        selectCustomers = Customer.objects.filter(first_name="Gary")    
        for c in selectCustomers:
            print(c.no)
            print(c.last_name)
            print(c.age)
        return HttpResponse(selectCustomers)    
         
    if (request.GET.get("first")):    
        c = Customer.objects.filter(first_name="Gary").first()
        print(c.no)
        print(c.last_name)
        print(c.age)
        return HttpResponse(f'{c.first_name} {c.last_name}-{c.age}')    
             
    return HttpResponse("none")