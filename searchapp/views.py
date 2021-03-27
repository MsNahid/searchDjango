from django.shortcuts import render
from django.http import HttpResponse

from .models import Musician

# Create your views here.
def home(request):
    musicians = Musician.objects.all()

    context = {
        'musicians': musicians

    }
    return render(request, 'searchapp/home.html', context)



