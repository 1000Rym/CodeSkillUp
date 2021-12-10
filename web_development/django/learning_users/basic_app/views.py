from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm 

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

def register(request):
    registerd = False
    
    if request.method == 'POST':
        # Check Validation of the data
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid(): 
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                
            profile.save()
            
            registerd = True
        else: 
            print("Erros, Occured(user_form, profile_form):",user_form.errors, profile_form.errors)        
        
       
    else: 
        user_form = UserForm()
        profile_form =UserProfileInfoForm()
    
    
    return render(request, 'basic_app/register.html', {'registered': registerd, 'user_form':user_form, 'profile_form':profile_form} )