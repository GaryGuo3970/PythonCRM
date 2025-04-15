from django import forms
from crm import models

class salesheader_ModelForm(forms.ModelForm):    
    class Meta:
        model = models.SalesHeader
        fields=["id","order_number","customer","currency","sales_date","total_amount","status","payment_status"]
