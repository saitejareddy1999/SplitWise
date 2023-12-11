from abc import ABC
import heapq
from collections import defaultdict

from SplitWiseProject.SplitWiseApp.Strategy.SettleUpStrategy import \
    SettleUpStrategy
from SplitWiseProject.SplitWiseApp.models import (ExpenseUser, Transaction,
                                                  Expenses,
                                                  )
from SplitWiseProject.SplitWiseApp.models.EUtype import EUtype


class Record:
    def __init__(self, user, amount):
        self.amount = amount
        self.user = user

    def __gt__(self, other):
        return self.amount > other.amount


class UserSettleUpStrategy(SettleUpStrategy, ABC):

    def __init__(self):
        self.expense_user = None

    def settle_up_heap(self, group_or_expenses_of_user):
        expenses = Expenses.objects.filter(group_or_expenses_of_user)
        expense_payed_by_users = []
        expense_had_to_pay = []
        for u_expense in expenses:
            payed_by = ExpenseUser.objects.filter(expense=u_expense, EUtype
            =EUtype.PAID_BY.value)
            had_to_pay = ExpenseUser.objects.filter(expense=u_expense, EUtype
            =EUtype.HAD_TO_PAY.value)
            expense_payed_by_users.extend(payed_by)
            expense_had_to_pay.extend(had_to_pay)
        extra_money = defaultdict()
        for paying_user in expense_payed_by_users:
            user = paying_user.user
            amount = paying_user.amount
            extra_money[user] += amount
        for paying_user in expense_had_to_pay:
            user = paying_user.user
            amount = paying_user.amount
            extra_money[user] -= amount
        pay_money_heap = []
        had_to_pay_heap = []
        transactions = []
        for user, amount in extra_money.items():
            record = Record(user, amount)
            if amount < 0:
                heapq.heappush(had_to_pay_heap, (-amount, record))
            if amount > 0:
                heapq.heappush(pay_money_heap, (amount, record))
        while len(pay_money_heap) and len(had_to_pay_heap):
            paying_record = heapq.heappop(pay_money_heap)
            receives_money = heapq.heappop(had_to_pay_heap)
            record = None
            if abs(paying_record[0]) > abs(receives_money[0]):
                transactions.append(Transaction(paying_record[1].user,
                                                receives_money[1].user,
                                                abs(receives_money[1].amount)))
                amount_left = abs(paying_record[1].amount) - abs(
                    receives_money[1].amount)
                record = Record(paying_record[1].user, amount_left)
                heapq.heappush(pay_money_heap, (amount_left, record))
            else:
                transactions.append(Transaction(paying_record[1].user,
                                                receives_money[1].user,
                                                abs(paying_record[1].amount)))
                amount_left = abs(receives_money[1].amount) - abs(
                    paying_record[1].amount)
                record = Record(receives_money[1].user, amount_left)
                heapq.heappush(had_to_pay_heap, (-amount_left, record))
            return transactions


    '''
      1.we want get id's from user 
      2.want to get how many expenses are there
      3.from those expenses we want to separate from  who is paying and 
      have_to _pay
      4.we want to minimize the transactions using heap
      '''
