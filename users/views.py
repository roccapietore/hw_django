import json
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.http import JsonResponse, request
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from hw import settings
from users.models import User, Location

json_params = {"ensure_ascii": False, "indent": 2}


class UserListView(ListView):
    model = User
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object_list = self.object_list.order_by("username").prefetch_related("locations").annotate(
            total_ads=Count('ad__is_published', filter=Q(ad__is_published=True)))

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        user_list = []
        for user in page_obj:
            user_list.append({
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "username": user.username,
                "password": user.password,
                "role": user.role,
                "age": user.age,
                "locations": [location.name for location in user.locations.all()],
                "total_ads": user.total_ads,
            })

        response = {
            "items": user_list,
            "total": paginator.count,
            "num_pages": paginator.num_pages
        }
        return JsonResponse(response, safe=False, json_dumps_params=json_params)


@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateView):
    model = User
    fields = ["first_name", "last_name", "username", "password", "role", "age", "locations"]

    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)

        new_user = User.objects.create(
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            username=user_data["username"],
            password=user_data["password"],
            role=user_data["role"],
            age=user_data["age"],
        )

        for location_name in user_data["locations"]:
            location, _ = Location.objects.get_or_create(name=location_name)
            new_user.locations.add(location)

        return JsonResponse({
            "id": new_user.id,
            "first_name": new_user.first_name,
            "last_name": new_user.last_name,
            "username": new_user.username,
            "password": new_user.password,
            "role": new_user.role,
            "age": new_user.age,
            "locations": [location.name for location in new_user.locations.all()]
        }, status=201, json_dumps_params=json_params)


class UserDetailView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        return JsonResponse({
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "password": user.password,
            "role": user.role,
            "age": user.age,
            "locations": [location.name for location in user.locations.all()]
        }, json_dumps_params=json_params)


@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ["first_name", "last_name", "username", "password", "role", "age", "locations"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        user_data = json.loads(request.body)
        self.object.first_name = user_data["first_name"]
        self.object.last_name = user_data["last_name"],
        self.object.username = user_data["username"],
        self.object.password = user_data["password"],
        self.object.role = user_data["role"],
        self.object.age = user_data["age"],
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "first_name": self.object.first_name,
            "last_name": self.object.last_name,
            "username": self.object.author.username,
            "password": self.object.password,
            "role": self.object.role,
            "age": self.object.age,
            "locations": [location.name for location in self.object.locations.all()]
        }, status=200, json_dumps_params=json_params)


@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=204)
