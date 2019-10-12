from django.shortcuts import render

# Create your views here.
def index(req):
	return render(req,"index.html")
def welcome(res):
	return render(res,"welcome.html")