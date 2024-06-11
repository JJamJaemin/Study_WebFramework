from .models import Sale
from django import forms
class SaleForm(forms.ModelForm):
    class Meta:             #ModelForm에서 상속받은 경우에 있어야함
        model = Sale
        fields = ('content', )