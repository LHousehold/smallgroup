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
      day=day) | Group.objects.filter(group_type="Co-ed", day=day)
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
  phone = request.GET.get('phone','c')

  leader_topic = "Smallgroup Signup from " + name
  #leader_emails = ['luke.household@gmail.com']
  leader_emails = ['zibak@catchthefire.com','szijl@catchthefire.com']
  #leader_emails = []
  #leader_emails.append(group.leader.email)
  #if group.leader2:
  #  leader_emails.append(group.leader2.email)

  leader_message = '''
  Hey there!

  There's a new signup request for a Central Small Group!

  Details are below:

  Name: %s
  Email: %s
  Phone: %s

  Group: %s

  I'm chuffed to bits to help you with your connection today!
  ''' %(name,email,phone,group.name)

  send_mail(leader_topic, leader_message, 'connect.central.ctf@gmail.com', leader_emails)

  # Send bounce back to new signup

  signup_topic = "Thanks for signing up for a Small Group!"

  signup_message = '''
  Hi there!

  Thank you so much for signing up for a Central Small Group! We are excited that you want to be part of our community!
  The Small Group Leader of your group will be in touch with you to give you more details on when the group meets, what it will be about and what you need to bring.
  If your Small Group leader hasn't reached out to you within 5 days, please let us know by emailing our Pastoral Intern Ziba Kanagasabapathy at zibak@catchthefire.com.

  Looking forward to see you at Central!

  Blessings,
  The Central Team
  '''

  send_mail(signup_topic, signup_message, 'connect.central.ctf@gmail.com', [email])

  return HttpResponse("0")




