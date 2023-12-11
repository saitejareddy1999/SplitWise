from django.db import models

from . import Expenses
from .BaseModel import BaseModel
from .User import User


class Group(BaseModel):
    name = models.CharField(max_length=255)
    # G_user = models.ManyToManyField(User, related_name='group_user')
    G_expense = models.ForeignKey('SplitWiseApp.Expenses',
                                  on_delete=models.CASCADE)  # one to many
    participants = models.ManyToManyField(User,
                                          related_name='group_participants')
    admin = models.ManyToManyField(User, related_name='group_admin')
    description = models.CharField(max_length=255)

    # Expense_User = models.ForeignKey('SplitWiseApp.ExpenseUser',
    # on_delete=models.CASCADE)

    @staticmethod
    def get_group_by_id(group_id):
        return Group.objects.filter(group_id)
