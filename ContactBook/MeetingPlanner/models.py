from django.db import models

# Create your models here.


class Planner(models.Model):
    user = models.ForeignKey("UserManager.MySuperUser", on_delete=models.CASCADE)
    contact = models.ForeignKey("PhoneBook.Contact", on_delete=models.CASCADE)
    title = models.CharField(max_length=200,null=False,blank=False,default=None)
    date = models.DateField()
    time = models.TimeField()
    address = models.CharField(max_length=300,null=True,blank=True,default="ONLINE")
    link = models.URLField(null=True,blank=True,default=None)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.title