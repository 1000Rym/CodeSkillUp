from django.shortcuts import render

# Create your views here.
def index(request):
    """
    Direct link to the home page
    """
    my_dict = {
        'text': 'hello world',
        'number': 100
    }
    return render(request, "basic_app/index.html", my_dict)


def relative(request):
    """
    Direct link to the relative page
    """
    return render(request, "basic_app/relative.html")

def other(request):
    """
    Direct link to the other page.
    """
    return render(request, "basic_app/other.html")
