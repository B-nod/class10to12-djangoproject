from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class CustomUser(AbstractBaseUser):

    role = models.IntegerField()


