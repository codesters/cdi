from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from cdi.home.models import *

North   = ['Jammu and Kashmir', 'Himachal Pradesh', 'Uttarakhand', 'Punjab', 'Haryana', 'Delhi', 'Uttar Pradesh']
East    = ['Assam', 'Meghalaya', 'Manipur', 'Mizoram', 'Nagaland', 'Sikkim', 'Tripura', 'Arunachal Pradesh', 'West Bengal']
West    = ['Rajasthan', 'Gujarat', 'Maharashtra', 'Goa']
Central = ['Madhya Pradesh', 'Bihar', 'Jharkhand', 'Chhattisgarh', 'Orissa', 'Karnataka']
South   = ['Kerala', 'Tamil Nadu', 'Andhra Pradesh']
region_dict = {
            1: North,
            2: East,
            3: West,
            4: Central,
            5: South,
            }

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
    try:
        clubs=Club.objects.filter(college__address__state__in =(region_dict[offset]))
    except (ValueError, ObjectDoesNotExist):
        raise Http404()
    if  clubs.count() == 0:
        raise Http404()
    return render_to_response('home/clubs/clubs_region.html', {'club_list': clubs }, context_instance = RequestContext(request))

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

##         EVENTS           ##

def events_all(request):
    event_list = Event.objects.all().order_by('name')
    paginator = Paginator(event_list, 3)

    page = request.GET.get('page')
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)
    return render_to_response('home/events/events_all.html', {'event_list': events}, context_instance=RequestContext(request))

def events_coming(request):
    event_list = Event.objects.all().order_by('start_date')
    paginator = Paginator(event_list, 3)

    page = request.GET.get('page')
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)
    return render_to_response('home/events/events_all.html', {'event_list': events}, context_instance=RequestContext(request))

def events_popular(request):
    event_list = Event.objects.all().order_by('-popularity', 'name')[:10]
    paginator = Paginator(event_list, 3)

    page = request.GET.get('page')
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)
    return render_to_response('home/events/events_all.html', {'event_list': events}, context_instance=RequestContext(request))

def events_campus(request, offset=1):
    try:
        events=Event.objects.filter(host__id__exact=int(offset))
    except (ValueError, ObjectDoesNotExist):
        raise Http404()
    if  events.count() == 0:
        raise Http404()
    cname = events[0].host.name
    return render_to_response('home/events/events_campus.html', {'cname': cname, 'event_list': events }, context_instance = RequestContext(request))

def events_region(request, offset=1):
    offset = int(offset)
    try:
        events=Event.objects.filter(host__address__state__in =(region_dict[offset]))
    except (ValueError, ObjectDoesNotExist):
        raise Http404()
    if  events.count() == 0:
        raise Http404()
    return render_to_response('home/events/events_type.html', {'event_list': events }, context_instance = RequestContext(request))

def events_types(request, offset=1):
    offset = int(offset)
    type_dict = {
            1: 'Academics',
            2:'Seminar/Workshop',
            3: 'Party',
            4: 'Festival',
            5: 'Conference',
            6: 'Competition',
            7: 'Other',
            }
    try:
        events=Event.objects.filter(event_type__exact=(type_dict[offset]))
    except (ValueError, ObjectDoesNotExist):
        raise Http404()
    if  events.count() == 0:
        raise Http404()
    etype = events[0].event_type
    return render_to_response('home/events/events_type.html', {'etype':etype, 'event_list': events }, context_instance = RequestContext(request))

def events_detail(request, offset=1):
    try:
        event = Event.objects.get(id=int(offset))
    except (ValueError, ObjectDoesNotExist):
        raise Http404()
    return render_to_response('home/events/event_detail.html', {'event': event }, context_instance = RequestContext(request))

##         COLLEGES           ##

def colleges_all(request):
    college_list = College.objects.all().order_by('name')
    paginator = Paginator(college_list, 3)

    page = request.GET.get('page')
    try:
        colleges = paginator.page(page)
    except PageNotAnInteger:
        colleges = paginator.page(1)
    except EmptyPage:
        colleges = paginator.page(paginator.num_pages)
    return render_to_response('home/colleges/colleges_all.html', {'college_list': colleges}, context_instance=RequestContext(request))

def colleges_popular(request):
    college_list = College.objects.all().order_by('-rating', 'name')[:10]
    paginator = Paginator(college_list, 3)

    page = request.GET.get('page')
    try:
        colleges = paginator.page(page)
    except PageNotAnInteger:
        colleges = paginator.page(1)
    except EmptyPage:
        colleges = paginator.page(paginator.num_pages)
    return render_to_response('home/colleges/colleges_popular.html', {'college_list': colleges}, context_instance=RequestContext(request))

def colleges_region(request, offset=1):
    offset = int(offset)
    try:
        colleges=College.objects.filter(address__state__in =(region_dict[offset]))
    except (ValueError, ObjectDoesNotExist):
        raise Http404()
    if  colleges.count() == 0:
        raise Http404()
    return render_to_response('home/colleges/colleges_region.html', {'college_list': colleges }, context_instance = RequestContext(request))

def colleges_types(request, offset=1):
    offset = int(offset)
    type_dict = {
            1: 'Arts/Commerce/Science',
            2: 'Engineering',
            3: 'Management',
            4: 'Law',
            5: 'Medical/Dental',
            6: 'Others',
            }
    try:
        colleges=College.objects.filter(college_type__exact=(type_dict[offset]))
    except (ValueError, ObjectDoesNotExist):
        raise Http404()
    if  colleges.count() == 0:
        raise Http404()
    cotype = colleges[0].college_type
    return render_to_response('home/colleges/colleges_type.html', {'cotype':cotype, 'college_list': colleges }, context_instance = RequestContext(request))

def colleges_detail(request, offset=1):
    try:
        college = College.objects.get(id=int(offset))
    except (ValueError, ObjectDoesNotExist):
        raise Http404()
    return render_to_response('home/colleges/college_detail.html', {'college': college }, context_instance = RequestContext(request))

##         Academics         ##

def notes_all(request):
    note_list = Note.objects.all().order_by('name')
    paginator = Paginator(note_list, 3)

    page = request.GET.get('page')
    try:
        notes = paginator.page(page)
    except PageNotAnInteger:
        notes = paginator.page(1)
    except EmptyPage:
        notes = paginator.page(paginator.num_pages)
    return render_to_response('home/academics/notes_all.html', {'note_list': notes}, context_instance=RequestContext(request))
             
def notes_course(request, offset=1):
    offset = int(offset)
    course_dict = {
            1: 'Computer Science',
            2: 'Electronics and Communication',
            3: 'Mechanical and Automation',
            4: 'Civil',
            5: 'Biotech',
            }
    try:
        notes=Note.objects.filter(related_course__exact=(course_dict[offset]))
    except (ValueError, ObjectDoesNotExist):
        raise Http404()
    if  notes.count() == 0:
        raise Http404()
    ncourse = notes[0].related_course
    return render_to_response('home/academics/notes_course.html', {'ncourse':ncourse, 'note_list': notes }, context_instance = RequestContext(request))
