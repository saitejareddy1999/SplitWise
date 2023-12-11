from django.http import JsonResponse
from django.views import View

from SplitWiseProject.SplitWiseApp.Services.SettleUpGroup import SettleUpGroup
from SplitWiseProject.SplitWiseApp.Services.SettleUpService import \
    SettleUpService


class SettleUpView(View):
    def post(self, request):
        user_id = request.POST.get("user_id")
        group_id = request.POST.get("group_id")
        try:
            expense = SettleUpService.settle_up_user(user_id)
            group = SettleUpGroup.settle_up_group(group_id)
            response_data = {
                'user_settlement': {
                    'message': 'settle up successful',
                    'expense_details': {
                        'id': expense.id,
                        'amount': expense.amount,
                    }
                },
                'group_settlement': {
                    'message': 'settle up successful',
                    'expense_details': {
                        'id': group.id,
                        'amount': group.amount,
                    }
                }
            }
            return JsonResponse(response_data)
        except:
            return JsonResponse({'error': 'not settled up successfully'})
