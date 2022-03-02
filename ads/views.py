import json
from django.http import JsonResponse, request
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
from ads.models import Ad, Category


json_params = {"ensure_ascii": False, "indent": 2}


class AdsView(View):
    def get(self, request):
        return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
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
        return JsonResponse(response, safe=False, json_dumps_params=json_params)

    def post(self, request):
        ad_data = json.loads(request.body)
        new_ad = Category()
        new_ad.name = ad_data["name"]
        new_ad.author = ad_data["author"]
        new_ad.price = ad_data["price"]
        new_ad.description = ad_data["description"]
        new_ad.address = ad_data["address"]
        new_ad.is_published = ad_data["is_published"]

        new_ad.save()

        return JsonResponse({
                "id": new_ad.pk,
                "name": new_ad.name,
                "author": new_ad.author,
                "description": new_ad.description,
                "address": new_ad.address,
                "is_published": new_ad.is_published,
        },  status=201, json_dumps_params=json_params)


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
            }, json_dumps_params=json_params)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        response = []
        for category in categories:
            response.append({
                "id": category.id,
                "name": category.name,
            })
        return JsonResponse(response, safe=False, json_dumps_params=json_params)

    def post(self, request):
        category_data = json.loads(request.body)
        new_category = Category()
        new_category.name = category_data["name"]
        new_category.save()

        return JsonResponse({
                "id": new_category.pk,
                "name": new_category.name,
        },  status=201, json_dumps_params=json_params)


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()
        return JsonResponse({
            "id": category.id,
            "name": category.name,
            }, json_dumps_params={"ensure_ascii": False, "indent": 2})
