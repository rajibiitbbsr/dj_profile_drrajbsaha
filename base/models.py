from django.db import models
from django.contrib.auth.models import User


class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    publications = models.CharField(max_length=1000)

    def __str__(self):
        return self.publications
    

# Create your models here.
