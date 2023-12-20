from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello_world(requests):
    print("Requests: ")
    print(requests)
    return HttpResponse("<h1>Heading 1</h1>")

def abhi_nandan(requests):
    print("Requests: ")
    print(requests)
    return HttpResponse("<h1>Hello Abhinandan</h1>")

def nav_bar(requests):
    return render(requests, "home/home.html")

def login(requests):
    return render(requests, "home/login.html")
