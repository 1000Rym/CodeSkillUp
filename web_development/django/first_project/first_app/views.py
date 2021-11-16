from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = {'first_template_app_contents':'This contents come from first_template_app/index.html'}

    # return HttpResponse("Hello Ben!")
    return render(request, 'first_template_app/index.html', context = my_dict)
