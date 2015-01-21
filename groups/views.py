from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader, Context, Template
from django.core.mail import send_mail

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

def contact(request):
  group_id = request.GET.get('id','c')
  group = Group.objects.get(id=group_id)
  name = request.GET.get('name','c')
  email = request.GET.get('email','c')
  topic = "Smallgroup Signup from " + name
  leader_emails = []
  leader_emails.append(group.leader.email)
  if group.leader2:
    leader_emails.append(group.leader2.email)

  message = '''
  Hey there!

  You have a new signup request for your group!

  Details are below:

  Name: %s
  Email: %s

  Group: %s

  I'm chuffed to bits to help you with your connection today!
  ''' %(name,email,group.name)

  send_mail(topic, message, 'connect.central.ctf@gmail.com', leader_emails)

  return HttpResponse("0")






