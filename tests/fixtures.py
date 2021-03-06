import pytest


@pytest.fixture()
@pytest.mark.django_db
def token(client, django_user_model):
    username = "username"
    password = "password"
    age = 30

    django_user_model.objects.create_user(username=username, password=password, age=age)

    response = client.post(
        "/user/token/",
        {"username": username, "password": password}, format="json")

    return response.data["access"], response.data["refresh"]
