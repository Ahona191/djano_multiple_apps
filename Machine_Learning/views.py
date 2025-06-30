from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here. 
def machine_learning(request): 
    return HttpResponse('<h1>Study Mart offering lot of free and paid courses</h1>')

def deep_learning(request): 
    return HttpResponse('We have full deep learning course') 

def about_us(request): 
    return HttpResponse('I have experiencs')
    
