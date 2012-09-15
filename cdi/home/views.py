from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from cdi.home.models import *

def clubs_all(request):
    club_list = Club.objects.all()
    paginator = Paginator(club_list, 3)

    page = request.GET.get('page')
    try:
        clubs = paginator.page(page)
    except PageNotAnInteger:
        clubs = paginator.page(1)
    except EmptyPage:
        clubs = paginator.page(paginator.num_pages)
    return render_to_response('home/clubs_test.html', {'club_list': clubs}, context_instance=RequestContext(request))

def clubs_detail(request, offset=1):
    try:
        club = Club.objects.get(id=int(offset))
    except (ValueError, ObjectDoesNotExist):
        raise Http404()
    return render_to_response('home/club_detail.html', {'club': club }, context_instance = RequestContext(request))
