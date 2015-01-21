from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader, Context, Template

from models import Group

# Create your views here.

def index(request):
  template = loader.get_template('groups/index.html')
  context = RequestContext(request, {})

  return HttpResponse(template.render(context))

def groups(request):
  group_type = request.GET.get('t','c')

  #retrieve dictionary of lists of groups based on days
  if group_type == 'm':
    group_type = 'Men'
  elif group_type == 'w':
    group_type = 'Women'
  else:
    group_type = 'Couples'

  #groups = Group.objects.filter(group_type = group_type)

  days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
  groups = {}
  for day in days:
    if group_type == 'Women' or group_type == 'Men':
      groups[day] = Group.objects.filter(group_type=group_type,
      day=day) | Group.objects.filter(group_type="Mixed", day=day)
    else:
      groups[day] = Group.objects.filter(group_type=group_type, day=day)

  template = loader.get_template('groups/groups.html')
  context = RequestContext(request, {"groups": groups})
  #template = Template(loader.get_template('groups/groups.html')
  #context = Context({"groups": groups})

  return HttpResponse(template.render(context))

def signup(request):
  group_id = request.GET.get('id','c')

  group = Group.objects.get(id=group_id)

  template = loader.get_template('groups/signup.html')
  context = RequestContext(request, {"group": group})

  return HttpResponse(template.render(context))

def thankyou(request):
  template = loader.get_template('groups/thankyou.html')
  context = RequestContext(request, {})

  return HttpResponse(template.render(context))