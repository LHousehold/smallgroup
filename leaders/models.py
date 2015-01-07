from django.db import models

# Create your models here.



class Leader(models.Model):
    genders = (('Male','Male'), ('Female','Female'))

    name = models.CharField(max_length=64)
    email = models.EmailField()
    gender = models.Field(max_length=12, choices=genders)

    def __str__(self):
        return self.name



class Picture(models.Model):
    leader = models.ForeignKey(Leader)
    filepath = models.ImageField()

    def __str__(self):
        return self.leader

