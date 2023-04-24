from django.shortcuts import render, redirect

# Create your views here.
def mainpg(request):
    return render(request, 'mainpg/mainpg.html')