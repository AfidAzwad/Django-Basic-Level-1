from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    diction = {}
    return render(request, 'app1/home.html', context = diction)

#showing a text line in home page
"""
def home(request):
    return HttpResponse("This is a intro of Django");
"""

#showing a text line in extension "/intro"
"""
def intro(request):
   return HttpResponse("This is a intro page");
"""