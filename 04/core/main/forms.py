from django import forms
from .models import Employees

class AddEmployee(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ['name', 'position', 'enlisted', 'department', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}), 
            'position': forms.TextInput(attrs={'class': 'form-input'}), 
            'department': forms.TextInput(attrs={'class': 'form-input'}), 
        }
    
    # name = forms.CharField(max_length=64, label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    # position = forms.CharField(max_length=64, label='Должность', widget=forms.TextInput(attrs={'class': 'form-input'}))
    # enlisted = forms.DateField(label='Дата зачисления')
    # department = forms.CharField(max_length=64, label='Департамент' , widget=forms.TextInput(attrs={'class': 'form-input'}))
    # is_active = forms.BooleanField(label='Активен')


class DelEmployee(forms.Form):
    ID = forms.IntegerField(label='ID')