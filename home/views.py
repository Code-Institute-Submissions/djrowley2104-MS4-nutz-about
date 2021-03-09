from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def mainsite(request):
    """ link to the mainsite page """

    return render(request, 'home/mainsite.html')    