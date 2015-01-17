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
  group_types = (('Men','Men'), ('Women','Women'), ('Couples','Couples'))
  days_of_week = (('Mon','Monday'), ('Tue','Tuesday'), ('Wed','Wednesday'),
  ('Thu','Thursday'), ('Fri','Friday'), ('Sat','Saturday'), ('Sun','Sunday'))

  # must be many to many in case of multiple leaders
  leader = models.ForeignKey(Leader)
  name = models.CharField(max_length=64, default="New Smallgroup")
  group_type = models.CharField(max_length=8, choices=group_types, default="Men")
  picture = models.ImageField(upload_to="images/", default="images/empty_room.jpg")
  location = models.CharField(max_length="32")
  day = models.CharField(max_length="12", choices=days_of_week)
  time = models.DateTimeField()

  def __str(self):
    return self.name