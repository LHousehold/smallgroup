from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from models import Leader

# Create your views here.

def index(request):
  template = loader.get_template('groups/index.html')
  context = RequestContext(request, {})

  return HttpResponse(template.render(context))