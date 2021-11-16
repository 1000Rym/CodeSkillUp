from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def users(request):
    users = User.objects.order_by('email')
    my_dict = {'users':users}
    return render(request,'users/index.html', my_dict)
