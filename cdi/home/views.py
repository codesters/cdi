from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from cdi.home.models import *

def clubs_all(request):
    club_list = Club.objects.all().order_by('?')
    paginator = Paginator(club_list, 3)

    page = request.GET.get('page')
    try:
        clubs = paginator.page(page)
    except PageNotAnInteger:
        clubs = paginator.page(1)
    except EmptyPage:
        clubs = paginator.page(paginator.num_pages)
    return render_to_response('home/clubs/clubs_all.html', {'club_list': clubs}, context_instance=RequestContext(request))

def clubs_popular(request):
    club_list = Club.objects.all().order_by('-popularity', 'name')[:10]
    paginator = Paginator(club_list, 3)

    page = request.GET.get('page')
    try:
        clubs = paginator.page(page)
    except PageNotAnInteger:
        clubs = paginator.page(1)
    except EmptyPage:
        clubs = paginator.page(paginator.num_pages)
    return render_to_response('home/clubs/clubs_all.html', {'club_list': clubs}, context_instance=RequestContext(request))

def clubs_campus(request, offset=1):
    try:
        clubs=Club.objects.filter(college__id__exact=int(offset))
    except (ValueError, ObjectDoesNotExist):
        raise Http404()
    if  clubs.count() == 0:
        raise Http404()
    cname = clubs[0].college.name
    return render_to_response('home/clubs/clubs_campus.html', {'cname': cname, 'club_list': clubs }, context_instance = RequestContext(request))

def clubs_region(request, offset=1):
    offset = int(offset)
    region_dict = {
            1: 'North',
            2: 'East',
            3: 'West',
            4: 'Central',
            5: 'South',
            }
    North = []
    East = []
    West = []
    Central = []
    South = []
    try:
        clubs=Club.objects.filter(club_type__exact=(type_dict[offset]))
    except (ValueError, ObjectDoesNotExist):
        raise Http404()
    if  clubs.count() == 0:
        raise Http404()
    ctype = clubs[0].club_type
    return render_to_response('home/clubs/clubs_type.html', {'ctype':ctype, 'club_list': clubs }, context_instance = RequestContext(request))

def clubs_types(request, offset=1):
    offset = int(offset)
    type_dict = {
            1: 'Engineering/Technology',
            2:'Applied Sciences',
            3: 'Social/NGO',
            4: 'Drama/Arts/Literature',
            5: 'Music/Bands',
            6: 'Management/Finance',
            7: 'Others',
            }
    MEMBERSHIP_CHOICE = (
        ('Open to anyone', 'Open to anyone'),
        ('Some Criteria', 'Some Criteria'),
        ('Through Apply and Selection', 'Through Apply and Selection'),
        ('Closed', 'Closed'),
            )
    try:
        clubs=Club.objects.filter(club_type__exact=(type_dict[offset]))
    except (ValueError, ObjectDoesNotExist):
        raise Http404()
    if  clubs.count() == 0:
        raise Http404()
    ctype = clubs[0].club_type
    return render_to_response('home/clubs/clubs_type.html', {'ctype':ctype, 'club_list': clubs }, context_instance = RequestContext(request))

def clubs_detail(request, offset=1):
    try:
        club = Club.objects.get(id=int(offset))
    except (ValueError, ObjectDoesNotExist):
        raise Http404()
    return render_to_response('home/clubs/club_detail.html', {'club': club }, context_instance = RequestContext(request))
