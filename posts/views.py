from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def list_post(request):
    posts=[1,2,3]
    return HttpResponse(str(posts))