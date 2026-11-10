from django import forms
from .models import Orders


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['full_name','email','address']
        