from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord

# Create your views here.
def index(request):

    access_records = AccessRecord.objects.order_by('date')

    my_dict = {
    'first_template_app_contents':'This contents come from first_template_app/index.html',
    'access_records': access_records
    }

    # return HttpResponse("Hello Ben!")
    return render(request, 'first_template_app/index.html', context = my_dict)
