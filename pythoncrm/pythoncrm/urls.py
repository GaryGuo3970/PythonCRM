"""
URL configuration for pythoncrm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.http import HttpResponse
from django.urls import path
from crm import views as crm_views
from finance import views as finance_views

urlpatterns = [
    ## 管理
    path('', crm_views.crm),   
    path('/', crm_views.crm),   
    path('crm', crm_views.crm),    
    path('login',crm_views.login),
    path('logout', crm_views.logout),
    
    ## 基础数据
    path('crm/dealertype', crm_views.dealerTypelist),
    path('crm/dealertypeadd', crm_views.dealerTypeAdd),    
    path('crm/dealertypedelete', crm_views.dealerTypeDelete),
    path('crm/dealertypeedit', crm_views.dealerTypeEdit),
    path('crm/dealer', crm_views.dealerlist),
    path('crm/dealeradd', crm_views.dealerAdd),
    path('crm/dealeredit', crm_views.dealerEdit),
    path('crm/dealerdelete', crm_views.dealerDelete),
    path('crm/department', crm_views.departmentlist),

    path('crm/customer', crm_views.customerlist),
    path('crm/customeradd', crm_views.customeradd),
    path('crm/customeredit', crm_views.customeredit),
    path('crm/customerdelete', crm_views.customerdelete),
    path('crm/douban', crm_views.douban),
    path('crm/db', crm_views.dbOperate),
    path('finance', finance_views.finance),
    path('admin/', admin.site.urls),
    path('crm/get',crm_views.GetStudy)
]
