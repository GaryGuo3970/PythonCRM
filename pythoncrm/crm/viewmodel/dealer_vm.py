from django import forms

from crm import models



class dealer_vm(forms.Form):
    dealer_id = forms.CharField(max_length=50, required=False,widget=forms.HiddenInput())
    dealer_name = forms.CharField(max_length=50, required=False,widget=forms.TextInput())
    dealer_address = forms.CharField(max_length=100, required=False,widget=forms.TextInput())
    dealer_phone = forms.CharField(max_length=15, required=False,widget=forms.PasswordInput())
    dealer_email = forms.EmailField(required=False)
    dealer_website = forms.URLField(required=False)
    dealer_contact_person = forms.CharField(max_length=50, required=False)
    dealer_contact_number = forms.CharField(max_length=15, required=False)
    dealer_contact_email = forms.EmailField(required=False)
    dealer_status = forms.ChoiceField(choices=[('active', 'Active'), ('inactive', 'Inactive')], required=False)

class dealer_ModelForm(forms.ModelForm):    
    # custom_name = forms.CharField(max_length=50, required=False,widget=forms.TextInput())
    # custom_status = forms.ChoiceField(choices=[('active', 'Active'), ('inactive', 'Inactive')], required=False)
    class Meta:
        model = models.Dealer
        fields=["id","no","name","address","phone","email","dealer_type"]

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['dealer_type'].queryset = models.Dealer_Type.objects.all()
    #     self.fields['custom_name'].widget.attrs.update({'placeholder': 'Enter custom name'})
    #     self.fields['custom_status'].widget.attrs.update({'placeholder': 'Select status'})

    #     for field_name, field in self.fields.items():
    #         field.widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned_data = super().clean()
        phone = '+58 '+cleaned_data.get("phone")
        if not phone:
            self.add_error('dealer_phone', "Dealer phone number is required.")
    