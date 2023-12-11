from django.db import models

from .BaseModel import BaseModel


class User(BaseModel):
    name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name
