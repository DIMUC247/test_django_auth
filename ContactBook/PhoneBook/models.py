from django.db import models

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100, null=True, default=None)
    address = models.TextField(null=True, default=None)
    user = models.ForeignKey("UserManager.MySuperUser", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.phone_number}"