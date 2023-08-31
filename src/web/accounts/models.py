from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class UserAccount(AbstractUser):
    id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return str(super().username)

    def __repr__(self):
        return '%s(%s)' % (
            self.__class__.__name__, 
            ', '.join([
                f'{key}={value}'
                for key, value in self.__dict__['__values__'].items()
            ])
        )
