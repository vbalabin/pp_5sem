from django.http import HttpResponse
from django.shortcuts import render

from main.forms import AddEmployee, DelEmployee
from main.models import Employees

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = DelEmployee(request.POST)
        if form.is_valid():

            try:
                ID = int(form['ID'].value())
                print(ID)
                Employees.objects.filter(id=ID).delete()
            except:
                form.add_error(None, 'KeyError')
                print('excepted')
    else:
        form = DelEmployee()

    employees = Employees.objects.all()
    return render(request, 'main/index.html', {'del_form': form, "employees": employees})

def addemployee(request):
    if request.method == 'POST':
        form = AddEmployee(request.POST, request.FILES)
        if form.is_valid():
            #print(form.cleaned_data)
            form.save()

    else:
        form = AddEmployee()

    return render(request, 'main/addemployee.html', {'add_form': form})