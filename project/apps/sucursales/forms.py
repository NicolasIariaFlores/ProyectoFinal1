from django import forms
from . import models

"""class PaisSucursalForm(forms.ModelForm):
    class Meta: 
        model = models.PaisSucursal
        fields = "__all__"
"""
class SucursalForm(forms.ModelForm): 
    class Meta: 
        model = models.Sucursal
        fields = "__all__"