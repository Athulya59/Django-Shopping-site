from django.shortcuts import render
from .models import Users,Login
from .forms import PostForm,GetForm
from django.shortcuts import redirect

def home(request):
	return render(request,'shop/home.html',{'home':home})

def signup(request):
	if request.method=="POST":
		form=PostForm(request.POST)
		email1=request.POST.get('email')
		if Users.objects.filter(email=email1).exists():
			error_message="User already exists.Login to continue"
			return redirect('/login')
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form=PostForm()
		return render(request,'shop/signup.html',{'form':form})

def login(request):
	if request.method == "POST":
		username1 = request.POST.get('username')
		password1  = request.POST.get('password')
		if Users.objects.filter(username=username1).exists():
			if Users.objects.filter(password=password1).exists():
				return redirect('/')
			else:
				return render(request,'shop/login.html',{'login':login,'error_message':"Invalid Password"})
		else:
			return render(request,'shop/login.html',{'login':login,'error_message':"Invalid Username/Password"})
	else:
		form=GetForm()
		return render(request,'shop/login.html',{'form':form})

def products(request):
	return render(request,'shop/products.html',{'products':products})