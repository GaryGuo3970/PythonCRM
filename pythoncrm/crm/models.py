from django.db import models

# Create your models here.

class Customer(models.Model):
    no= models.CharField(max_length=10, unique=True,validators=[], blank=True, null=True,verbose_name="客户编号")
    first_name = models.CharField(max_length=100,validators=[], blank=True, null=True,verbose_name="名")
    last_name = models.CharField(max_length=100,verbose_name="姓")
    email = models.EmailField(validators=[], blank=True, null=True,verbose_name="邮箱")
    phone = models.CharField(max_length=20, blank=True, null=True,verbose_name="电话")
    address = models.TextField(blank=True, null=True,verbose_name="地址")
    age =models.IntegerField(blank=True, null=True,verbose_name="年龄")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="更新时间")
    is_active = models.BooleanField(default=True,verbose_name="是否激活")
    is_deleted = models.BooleanField(default=False,verbose_name="是否删除")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class SalesHeader(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,related_name="sales_headers",verbose_name="客户")
    order_number = models.CharField(max_length=20, unique=True,verbose_name="订单号")
    currency = models.CharField(max_length=3, default="",verbose_name="货币")
    sales_date = models.DateField(verbose_name="销售日期")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="总金额")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="更新时间")

    def __str__(self):
        return f"SalesHeader {self.id} - {self.customer}"