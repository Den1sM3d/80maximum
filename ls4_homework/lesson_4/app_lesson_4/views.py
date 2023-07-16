from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def ls4_homework_response(requests):
    return HttpResponse("домашка к 4 уроку")
