from django.shortcuts import render, redirect

def landing(request):
    return render(request, "hub/landing.html")

def home(request):
    return render(request, "hub/dashboard.html")

def listing(request):
    return render(request, "hub/listing.html")