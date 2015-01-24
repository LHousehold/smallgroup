from django.db import models

# Create your models here.
class Leader(models.Model):
  genders = (('Male','Male'), ('Female','Female'))

  name = models.CharField(max_length=64)
  email = models.EmailField()
  gender = models.CharField(max_length=12, choices=genders, default='Male')
  picture = models.ImageField(upload_to="images/", default="images/blank_avatar.gif")

  def __str__(self):
    return self.name


class Group(models.Model):
  group_types = (('Men','Men'), ('Women','Women'), ('Couples','Couples'), ('Co-ed','Co-ed'))
  days_of_week = (('Mon','Monday'), ('Tue','Tuesday'), ('Wed','Wednesday'),
  ('Thu','Thursday'), ('Fri','Friday'), ('Sat','Saturday'), ('Sun','Sunday'))

  leader = models.ForeignKey(Leader, related_name="leader_%(class)s_related")
  leader2 = models.ForeignKey(Leader, blank="True", null="True",
  related_name="leader2_%(class)s_related")
  coordinator = models.CharField(max_length=64, blank="True", null="True")
  name = models.CharField(max_length=64, default="")
  group_type = models.CharField(max_length=8, choices=group_types, default="Men")
  picture = models.ImageField(upload_to="images/", default="images/empty_room.jpg")
  location = models.CharField(max_length="32", null="True", blank="True")
  day = models.CharField(max_length="12", choices=days_of_week)
  time = models.CharField(max_length="8")
  description = models.CharField(max_length="1280", default="")
  address = models.CharField(max_length="32", default="")
  book = models.CharField(max_length="64", blank="True", null="True")

  def __str(self):
    return self.name