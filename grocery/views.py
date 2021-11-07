from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import *
from .forms import  CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import joblib
from models_and_data import model


def registerPage(request):
	form = CreateUserForm()

	if request.method == 'POST':
		print("hello")
		form = CreateUserForm(request.POST)
		
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			role = form.cleaned_data.get('first_name')
			print("username=",username,"password=",password,"role=",role)
			
			

			messages.success(request, 'Account was created for ' + username)
			return redirect('login')
	context = {'form':form}



	return render(request, 'register.html', context)
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
def login_request(request):
	if request.method == 'POST':
		
		username = request.POST.get('username')
		password =request.POST.get('password1')
		role = request.POST.get('first_name')
	

		
		
		

		user = authenticate(request, username=username, password=password)



		

		if user is not None:
			print("hey yo....",user.id)
			context={'userid':user.id}

			return render(request, 'home.html', context)

		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'login.html', context)

def result(request,pk):
	x=joblib.load("finalized_model.sav")
	lis=pk
	print(lis)
	print(model.fun(lis)['Title'].head())
	

	

	
	return render(request,"result.html")