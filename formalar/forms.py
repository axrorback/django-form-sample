from django import forms
from .models import Savollar

class SavollarForm(forms.ModelForm):
    class Meta:
        model = Savollar
        fields = '__all__'