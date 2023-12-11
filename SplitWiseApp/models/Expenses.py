from django.db import models

from . import Group
from .User import User
from .BaseModel import BaseModel
from .Type import Type


class Expenses(BaseModel):
    description = models.CharField(max_length=255)
    amount = models.FloatField()
    type = models.CharField(max_length=230, choices=[(type.name, type.value) for
                                                     type in
                                                     Type])
    history = models.CharField(max_length=255)
    # expense : user
    # m : 1
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # created_at = models
    users = models.ManyToManyField(User,related_name = 'involved_expenses')
    # group = models.ForeignKey('SplitWiseApp.Group', on_delete=models.CASCADE)
    Expense_User = models.ForeignKey("SplitWiseApp.ExpenseUser",
                                     on_delete=models.CASCADE)
