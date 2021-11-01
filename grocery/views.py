from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import *


def registerPage(request):

	return render(request,'register.html')
def grocery(request,pk):
	objs=grocery_store.objects.all()
	list=[]
	for i in objs:
		if(i.Category not in list):
			list.append(i.Category)
	context={}
	for i in range(0,len(list)):
		x=grocery_store.objects.filter(Category=pk)
		

	
	
	num={'x':x}
	return render (request,"grocery.html",num)
def home(request):
	return render (request,"home.html")
