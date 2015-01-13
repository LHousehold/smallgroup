from django.db import models

# Create your models here.



class Leader(models.Model):
    genders = (('Male','Male'), ('Female','Female'))

    name = models.CharField(max_length=64)
    email = models.EmailField()
    gender = models.CharField(max_length=12, choices=genders, default='Male')
    picture = models.ImageField(upload_to="images/", default="images/blank_avatar.jpg")

    def __str__(self):
        return self.name

