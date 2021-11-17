from django.shortcuts import render
from AppTwo.models import User
from AppTwo.forms import NewUser

# Create your views here.
def index(request):
    return render(request, 'index.html')

def users(request):
    users = User.objects.order_by('email')
    my_dict = {'users':users}
    return render(request,'users/index.html', my_dict)

def register(request):
    form = NewUser()

    if request.method == 'POST':
        form = NewUser(request.POST)

        if form.is_valid():
            # save form and commit to the database.
            form.save(commit=True)
            return users(request)
        else :
            print("Wrong format")

    return render(request, 'register.html', {'form':form})
