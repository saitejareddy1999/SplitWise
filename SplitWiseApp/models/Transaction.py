from django.db import models

from . import User
from .BaseModel import BaseModel


class Transaction(BaseModel):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()

    class Meta:
        abstract = True
