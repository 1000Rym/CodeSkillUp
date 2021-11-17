from django.shortcuts import render
from basicapp.form import FormName

# Create your views here.
def index(request):
    return render(request, 'basicapp/index.html')

def form_page(request):
    form = FormName()

    if request.method == 'POST' :
        form = FormName(request.POST)

        if form.is_valid():
            # Get the data from the cleaned_data
            print("Name:",form.cleaned_data['name'])
            print("Email:",form.cleaned_data['email'])
            print("Text",form.cleaned_data['text'])

    return render(request, 'basicapp/form_page.html', {'form':form})
