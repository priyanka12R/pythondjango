from django.shortcuts import render

from django.http import HttpResponse

def index(Request):
	return HttpResponse('You are at Index page.');

def home(Request):
	return HttpResponse("You are at home page.");


def contact(Request):
	return HttpResponse('You are at contact page.');


# Create your views here.
