from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse

# Create your views here.

# function view
# def index(request):
#     return render(request, 'index.html')

# Class View
# class CBView(View):
#     def get(self, request):
#         return HttpResponse("Class Based Views Are Cool!")

# Template View
class CBTView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['inject_me'] = "Basic Injection"
        
        return context
    