from django.db import models

# Create your models here.
class login_table(models.Model):

    name = models.CharField(max_length=256, unique=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=15)


    def __str__(self):
        return self.name
