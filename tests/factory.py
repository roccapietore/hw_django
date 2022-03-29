import factory
from ads.models import Ad, Category
from selection.models import Selection
from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    password = "test_password"
    age = 30


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("name")


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = "namenamename"
    price = 2500
    is_published = False
    author = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)


class SelectionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Selection

    name = "selection"
    owner = factory.SubFactory(UserFactory)
    items = factory.SubFactory(AdFactory)


