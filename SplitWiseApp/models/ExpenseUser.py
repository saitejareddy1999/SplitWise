from django.db import models
from .BaseModel import BaseModel
from .EUtype import EUtype
from .Expenses import Expenses
from .User import User


class ExpenseUser(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expense = models.ForeignKey(Expenses, on_delete=models.CASCADE)
    amount = models.FloatField()
    EU_type = models.CharField(max_length=255,
                               choices=[(type.name, type.value) for type in
                                        EUtype])


    @staticmethod
    def get_all_by_id(user_id):
        return ExpenseUser.objects.filter(user_id=user_id)
