from django.http.response import HttpResponse
from django.shortcuts import render

class Task:
    math = {
        'add': lambda a, b: a + b,
        'sub': lambda a, b: a - b,
        'mul': lambda a, b: a * b,
        'div': lambda a, b: a / b,
    }

    def __init__(self, request):
        res = request.GET
        self.a = None
        self.b = None
        self.m = None
        if 'op1' in res: self.a = res['op1']
        if 'op2' in res: self.b = res['op2']
        if 'math' in res: self.m = res['math']

    def calculate(self):
        a = float(self.a)
        b = float(self.b)
        return self.math[self.m](a, b)
        

# Create your views here.
def calculator(request):
    rg = request.GET
    if rg:
        task = Task(request)
        response = {
            'a': task.a,
            'b': task.b,
            'm': rg['math'],
            'result': task.calculate(),
        }        
    else:
        response = {
            'result': None,
        }


    return render(request, 'index.htm', response)
