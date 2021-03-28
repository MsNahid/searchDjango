from django.shortcuts import render
from django.http import HttpResponse

from .models import Musician

# Create your views here.
def home(request):
    # musicians = Musician.objects.order_by('-list_date')
    
    # Keyword Search
    

    # User Search
    balam_query = None
    if 'Balam' in request.GET:
        Balam = request.GET['Balam']
        if Balam:
           balam_query = Musician.objects.filter(name__icontains=Balam)

    habib_query = None
    if 'Habib' in request.GET:
        Habib = request.GET['Habib']
        if Habib:
           habib_query = Musician.objects.filter(name__icontains=Habib)


    tapos_query = None
    if 'Tapos' in request.GET:
        Tapos = request.GET['Tapos']
        if Tapos:
           tapos_query = Musician.objects.filter(name__icontains=Tapos)
    
    user_query = None
    if balam_query and habib_query and tapos_query:
        user_query = balam_query.union(habib_query, tapos_query).order_by('-list_date')
    elif balam_query and habib_query:
        user_query = balam_query.union(habib_query)
    elif habib_query and tapos_query:
        user_query = habib_query.union(tapos_query)
    elif balam_query and tapos_query:
        user_query = balam_query.union(tapos_query)
    elif balam_query:
        user_query = balam_query
    elif tapos_query:
        user_query = tapos_query
    elif habib_query:
        user_query = habib_query
    
    # user search end



    # # musicians = balam_query.union(habib_query, tapos_query).order_by('-list_date')
    # musicians = balam_query
    # if tapos_query:
    #     musicians = musicians.union(tapos_query)
    context = {
        'musicians': user_query
    }
    return render(request, 'searchapp/home.html', context)



