from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 32, unique = True)
    last_name = models.CharField(max_length = 32, unique = False)
    email = models.CharField(max_length = 64, unique = True)

    def __str__(self):
        return  self.first_name + " " + self.last_name\
                + "\nemail:" + self.email
