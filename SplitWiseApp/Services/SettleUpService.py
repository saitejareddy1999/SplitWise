from typing import List

from SplitWiseProject.SplitWiseApp.Strategy.SettleUpStrategy import \
    SettleUpStrategy
from SplitWiseProject.SplitWiseApp.models import User, ExpenseUser, Transaction, \
    Group


class SettleUpService:
    @staticmethod
    def settle_up_user(user_id):
        user = User.objects.filter(user_id)  # we can get all the users w.r.t
        # id's
        expense_user = ExpenseUser.get_all_by_id(user)  # per user what are
        # expense are there fetching
        expense = []
        for Expense_User in expense_user:
            expense.append(Expense_User.expense)
        transactions_list: List[Transaction] = (
            SettleUpStrategy.settle_up_heap(expense))
        filtered_transactions = []
        for transactions in transactions_list:
            if transactions.sender == user and transactions.receiver == user:
                filtered_transactions.append(transactions)
        return filtered_transactions

    @staticmethod
    def settle_up_group(group_id):
        group = Group.objects.filter(group_id)
        group_data = Group.get_group_by_id(group)
        group_info = []
        for gr in group_data:
            group_info.append(gr.Expense_User)
        transactions_list: List[Transaction] = (
            SettleUpStrategy.settle_up_heap(group_info))
        return transactions_list

    '''
    1.get all the expenses that this user is part of
    2.Iterate through all expenses & find out all the people involved how 
    much they are owned/owes ny each
    3.calling min/max heap algom to calculate the list of transactions
    4.return the list of transaction
    '''
