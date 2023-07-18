from django.shortcuts import render

# Create your views here.

def example(request):
    return render(request, "index.html")

def top_sellers(request):
    return render(request, 'top-sellers.html')