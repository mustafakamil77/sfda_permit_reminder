#forms.py

from django import forms    
from .models import SdfaPermit
from django.forms import DateInput

class NewPermitForm(forms.ModelForm):
    application_date = forms.DateField(widget=DateInput(attrs={'type': 'date'}),input_formats=['%Y-%m-%d'])
    release_date = forms.DateField(widget=DateInput(attrs={'type': 'date'}),input_formats=['%Y-%m-%d'])
    expiry_date = forms.DateField(widget=DateInput(attrs={'type': 'date'}),input_formats=['%Y-%m-%d'])
    application_date = forms.DateField(widget=DateInput(attrs={'type': 'date'}),input_formats=['%Y-%m-%d'])
    renewal_date = forms.DateField(widget=DateInput(attrs={'type': 'date'}),input_formats=['%Y-%m-%d'])

    class Meta:
        model = SdfaPermit
        fields =['company_name','application_date','transaction_number','status','invoice_number'
                 ,'notes','release_date','expiry_date','renewal_date'
]