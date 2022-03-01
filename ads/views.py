from django.http import JsonResponse
from django.views import View


class AdsView(View):
    def get(self):
        return JsonResponse({"status": "ok"}, status=200)
