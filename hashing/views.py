from pickle import GET
from django.http import HttpResponse
from django.shortcuts import render
import hashlib
def home(request):
    if request.method!=GET:
        name=request.GET.get('name','default')
        a=hashlib.sha256(f"{name}".encode('utf-8')).hexdigest()
        
    else:
        a="no data found"
    data={"name":name,"hash":a}
    return render(request,'index.html',data)