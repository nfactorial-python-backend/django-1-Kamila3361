from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def nfactorial(request):
    return HttpResponse("Hello, nfactorial school!")

def add(request, first, second):
    return HttpResponse(first + second)

def transform(request, text):
    return HttpResponse(text.upper())

def palindrome(request, word):
    return HttpResponse(word == word[::-1])

def calculator(request, first, operation, second):
    if operation == "add":
        return HttpResponse(first + second)
    if operation == "sub":
        return HttpResponse(first - second)
    if operation == "mult":
        return HttpResponse(first * second)
    if operation == "div" and second != 0:
        return HttpResponse(first / second)
    

