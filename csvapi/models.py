from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.


class Users(models.Model):
    user_id =models.UUIDField(primary_key=True, default=uuid.uuid4 ,unique=True, editable=False)
    name = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField(unique=True)
    
    
    def __str__(self):
        return f"{self.name} - {self.age} - {self.email}"
    
    
    


