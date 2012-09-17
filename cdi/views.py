from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def extra(request):
    #data = 'this is my data:', request
    return render_to_response('meta.html', context_instance=RequestContext(request))

