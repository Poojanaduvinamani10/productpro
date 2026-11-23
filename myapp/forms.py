from myapp.models import Product
from django import forms
class ProductForm(forms.ModelForm):
    class Meta:
        model= Product
        fields='__all__'

# class Product(forms.Form):
#     name=forms.CharField()
#     price=forms.IntegerField()
#     quantity=forms.IntegerField()
#     img=forms.ImageField()