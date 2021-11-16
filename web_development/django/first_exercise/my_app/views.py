from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<em>Hello, This is the first exercise page</em>")

def help(request):
    my_dict = {'intro':'Welcome to the help page.'}
    return render(request, 'help/index.html', my_dict)
