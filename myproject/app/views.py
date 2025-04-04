from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from django.shortcuts import redirect


# Create your views here.

def home(request):
    x="<h1>hello.... </h1>"
    return HttpResponse(x)



def about(request):
    data={'name':True,'age':False, 'quali':None}
    return JsonResponse(data)


# def index(request):
#     return render(request, 'index.html')


def otherpage(request):
    return redirect('https://www.google.com')




def index(request):
    data=[{'name':'raj', 'city':'delhi'},{'name':'abhi', 'city':'bpl'}]
    return render(request, 'index.html',{'key1':data})
