from django.http import HttpResponse
from django.shortcuts import render

from main.forms import AddEmployee, DelEmployee

# Create your views here.
def index(request):
    add_form = AddEmployee()
    del_form = DelEmployee()
    return render(request, 'main/index.html', {'add_form': add_form, 'del_form': del_form})

