from django.shortcuts import render
from .models import Advertisement
from .forms import AdvertisementForm
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import admin

# Create your views here.

def example(request):
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, "index.html", context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse("main-page")
            return redirect(url)
    else:
        form = AdvertisementForm()

    context = {"form": form}
    return render(request, "advertisement-post.html", context)