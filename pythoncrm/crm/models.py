from django.db import models

# Create your models here.
class ModelBase(models.Model):
    """ 模型基类 """
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="更新时间")
    is_active = models.BooleanField(default=True,verbose_name="是否激活")
    is_deleted = models.BooleanField(default=False,verbose_name="是否删除")

    class Meta:
        abstract = True
        verbose_name = "模型基类"

class Customer(ModelBase):
    no= models.CharField(max_length=10, unique=True,validators=[], blank=True, null=True,verbose_name="客户编号")
    first_name = models.CharField(max_length=100,validators=[], blank=True, null=True,verbose_name="名")
    last_name = models.CharField(max_length=100,verbose_name="姓")
    email = models.EmailField(validators=[], blank=True, null=True,verbose_name="邮箱")
    phone = models.CharField(max_length=20, blank=True, null=True,verbose_name="电话")
    address = models.TextField(blank=True, null=True,verbose_name="地址")
    age =models.IntegerField(blank=True, null=True,verbose_name="年龄")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class SalesHeader(ModelBase):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,related_name="sales_headers",verbose_name="客户")
    order_number = models.CharField(max_length=20, unique=True,verbose_name="订单号")
    currency = models.CharField(max_length=3, default="",verbose_name="货币")
    sales_date = models.DateField(verbose_name="销售日期")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="总金额")

    def __str__(self):
        return f"SalesHeader {self.id} - {self.customer}"

class Admin(ModelBase):
    """ 管理员表 """
    username = models.CharField(verbose_name="用户名",max_length=50)
    password = models.CharField(verbose_name="密码",max_length=100)
    email = models.EmailField(verbose_name="邮箱",max_length=100)
    phone = models.CharField(verbose_name="电话",max_length=50)
    def __str__(self):
        return self.username
    
class Dealer_Type(ModelBase):
    """ 经销商类型表 """
    no= models.CharField(max_length=20, unique=True,validators=[], blank=True, null=True,verbose_name="编号")
    name = models.CharField(verbose_name="名称",max_length=50)
    description = models.TextField(verbose_name="描述")
    category = models.SmallIntegerField(verbose_name="分类",choices=((1,"2S"),(2,"3S"),(3,"4S")))

    def get_category_display(self):
        CATEGORY_CHOICES = {
            1: '2S',
            2: '3S',
            3: '4S'
        }
        return CATEGORY_CHOICES.get(self.category, str(self.category))

class Dealer(ModelBase):
    """ 经销商表 """
    no= models.CharField(max_length=20, unique=True,validators=[], blank=True, null=True,verbose_name="经销商编号")
    name = models.CharField(verbose_name="名称",max_length=50)
    address = models.TextField(verbose_name="地址")
    phone = models.CharField(verbose_name="电话",max_length=50)
    email = models.EmailField(verbose_name="邮箱",max_length=100)
    dealer_type = models.ForeignKey(verbose_name="经销商类型",to="Dealer_Type",to_field="id",on_delete=models.DO_NOTHING)

class Department(ModelBase):
    """ 部门表 """
    no= models.CharField(max_length=20, unique=True,validators=[], blank=True, null=True,verbose_name="经销商编号")
    name = models.CharField(verbose_name="名称",max_length=50)

class Assert(models.Model):
    """ 资产表 """
    name = models.CharField(verbose_name="名称",max_length=50)
    price=models.IntegerField(verbose_name="价格")
    category = models.SmallIntegerField(verbose_name="资产类型",choices=((1,"房产"),(2,"机器设备"),(3,"运输工具"),(4,"电子产品"),(5,"办公设备"),(6,"土地")))
    department = models.ForeignKey(verbose_name="所属部门",to="Department",to_field="id",on_delete=models.CASCADE)