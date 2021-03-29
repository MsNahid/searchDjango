from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, timedelta
from django.db.models import Q

from .models import Musician

# Create your views here.
def home(request):
    # musicians = Musician.objects.order_by('-list_date')
    
    # Keyword Search
    keyone = None
    if 'Che1' in request.GET:
        Che1 = request.GET['Che1']
        if Che1:
            keyone = Musician.objects.filter(Q(keywords=Che1) & Q(keyword_occurrence=4))
    
    keytwo = None
    if 'Che2' in request.GET:
        Che2 = request.GET['Che2']
        if Che2:
            keytwo = Musician.objects.filter(Q(keywords=Che2) & Q(keyword_occurrence=10))

    keythree = None
    if 'Che3' in request.GET:
        Che3 = request.GET['Che3']
        if Che3:
            keythree = Musician.objects.filter(Q(keywords=Che3) & Q(keyword_occurrence=2))
    
    keyword_query = None
    if keyone and keytwo and keythree:
        keyword_query = keyone.union(keytwo, keythree)
    elif keyone and keytwo:
        keyword_query = keyone.union(keytwo)
    elif keytwo and keythree:
        keyword_query = keytwo.union(keythree)
    elif keyone and keythree:
        keyword_query = keyone.union(keythree)
    elif keyone:
        keyword_query = keyone
    elif keytwo:
        keyword_query = keytwo
    elif keythree:
        keyword_query = keythree    

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

    # Time range
    data_yesterday = None
    if 'Yesterday' in request.GET:
        Yesterday = request.GET['Yesterday']
        if Yesterday:
            yestr = date.today() - timedelta(days=1)
            data_yesterday = Musician.objects.filter(list_date__lt=date.today(), list_date__gt=yestr)

    data_last_week = None
    if 'Lastwk' in request.GET:
        Lastwk = request.GET['Lastwk']
        if Lastwk:
            wk = date.today() - timedelta(days=7)
            lastwk =  date.today() - timedelta(days=14)
            data_last_week = Musician.objects.filter(list_date__lte=wk, list_date__gte=lastwk)
    
    data_last_month = None
    if 'Lastmn' in request.GET:
        Lastmn = request.GET['Lastmn']
        # print(type(Lastmn))
        # print(Lastmn)
        if Lastmn:
            month = date.today() - timedelta(days=30)
            lastmonth = date.today() - timedelta(days=60)
            data_last_month =  Musician.objects.filter(list_date__lte=month, list_date__gte=lastmonth)
    
    time_range_query = None
    if data_yesterday and data_last_week and data_last_month:
        time_range_query = data_yesterday.union(data_last_month, data_last_month).order_by('-list_date')
    elif data_yesterday and data_last_week:
        time_range_query = data_yesterday.union(data_last_week).order_by('-list_date')
    elif data_last_week and data_last_month:
        time_range_query = data_last_week.union(data_last_month).order_by('-list_date')
    elif data_yesterday and data_last_month:
        time_range_query = data_yesterday.union(data_last_month).order_by('-list_date')
    elif data_yesterday:
        time_range_query = data_yesterday
    elif data_last_week:
        time_range_query = data_last_week
        # print("union")
    elif data_last_month:
        time_range_query = data_last_month
        print("union")

    # Date range
    date_range_query = None
    if 'startDate' in request.GET and 'endDate' in request.GET:
        startDate = request.GET['startDate']
        endDate = request.GET['endDate']
        # print(type(endDate))
        # print(startDate)
        if startDate and endDate:
            date_range_query = Musician.objects.filter(list_date__range=[startDate, endDate]).order_by('-list_date')
            
    musicians = None
    if keyword_query and user_query and time_range_query and date_range_query:
        musicians = keyword_query.intersection(user_query, time_range_query, date_range_query)
    elif keyword_query and user_query and time_range_query:
        musicians = keyword_query.intersection(user_query, time_range_query)
    elif user_query and time_range_query and date_range_query:
        musicians = user_query.intersection(time_range_query, date_range_query)
    elif keyword_query and time_range_query and date_range_query:
        musicians = keyword_query.intersection(time_range_query, date_range_query)
    elif keyword_query and user_query and date_range_query:
        musicians = keyword_query.intersection(user_query, date_range_query)
    elif keyword_query and user_query:
        musicians = keyword_query.intersection(user_query)
    elif keyword_query and time_range_query:
        musicians = keyword_query.intersection(time_range_query)
    elif keyword_query and date_range_query:
        musicians = keyword_query.intersection(date_range_query)
    elif user_query and time_range_query:
        musicians = user_query.intersection(time_range_query)
    elif user_query and date_range_query:
        musicians = user_query.intersection(date_range_query)
    elif time_range_query and date_range_query:
        musicians = time_range_query.intersection(date_range_query)
    elif keyword_query:
        musicians = keyword_query
    elif user_query:
        musicians = user_query
    elif time_range_query:
        musicians = time_range_query
        # print('intersection')
    elif date_range_query:
        musicians = date_range_query
    else:
        musicians = Musician.objects.order_by('-list_date')

    context = {
        'musicians':musicians
    }
    return render(request, 'searchapp/home.html', context)



