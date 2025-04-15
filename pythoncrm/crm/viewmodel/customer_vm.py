from django import forms
from crm import models
from django.core.exceptions import ValidationError

class customer_ModelForm(forms.ModelForm):    
    class Meta:
        model = models.Customer
        fields=["id","no","first_name","last_name","email","phone","address","age"]
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age'}),
        }

    def clean_phone(self):
        value = self.cleaned_data.get("phone")
        if len(value) != 11:
            raise ValidationError("手机号码不符合要求")
        return value