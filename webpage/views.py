from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'webpage/home.html')

def posts(request):
    return render(request, 'webpage/posts.html')

def post(request):
    return render(request, 'webpage/post.html')

def profile(request):
    return render(request, 'webpage/profile.html')