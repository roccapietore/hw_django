from django.http import JsonResponse
from django.views import View
from django.views.generic import DetailView

from ads.models import Ad, Category


class AdsView(View):
    def get(self):
        return JsonResponse({"status": "ok"}, status=200)


class AdView(View):
    def get(self, request):
        ads = Ad.objects.all()
        response = []
        for ad in ads:
            response.append({
                "id": ad.id,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price,
            })
        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 2})


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published,
            }, json_dumps_params={"ensure_ascii": False, "indent": 2})


class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        response = []
        for category in categories:
            response.append({
                "id": category.id,
                "name": category.name,
            })
        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 2})


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()
        return JsonResponse({
            "id": category.id,
            "name": category.name,
            }, json_dumps_params={"ensure_ascii": False, "indent": 2})
