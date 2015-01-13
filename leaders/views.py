from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from models import Leader

# Create your views here.


def index(request):
    leaders = Leader.objects.all()

    template = loader.get_template('leaders/index.html')
    context = RequestContext(request, {'leaders': leaders})
    return HttpResponse(template.render(context))

def leader(request):
    leader_id = request.GET.get('l', '')
    leader = Leader.objects.filter(id=leader_id)
    if leader:
        leader = leader[0]

    template = loader.get_template('leaders/leader.html')
    context = RequestContext(request, {'leader': leader})
    return HttpResponse(template.render(context))
