from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.


def index(request):
    """ A view to return the index page """
    if request.user.is_authenticated:
        return redirect('products')
    return render(request, 'home/index.html')


def mainsite(request):
    """ A view to return the index page """

    return render(request, 'home/mainsite.html')
