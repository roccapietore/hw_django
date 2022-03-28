import pytest


@pytest.mark.django_db
def test_create_ad(client, user, category):
    expected_response = {
        "name": "namenamename",
        "author": user.id,
        "price": 2500,
        "is_published": False,
        "description": None,
        "category": category.id,
        "image": None
        }

    data = {
            "id": 1,
            "name": "namenamename",
            "author": user.id,
            "price": 2500,
            "is_published": False,
            "description": None,
            "category": category.id}

    response = client.post(
        "/ad/create_ad/",
        data,
        content_type="application/json",

    )

    assert response.status_code == 201
    assert response.data == expected_response


@pytest.mark.django_db
def test_create_ad_incorrect_price(client, user, category):
    data = {
            "id": 1,
            "name": "namenamename",
            "author": user.id,
            "price": -2500,
            "is_published": False,
            "description": None,
            "category": category.id}

    response = client.post(
        "/ad/create_ad/",
        data,
        content_type="application/json",

    )
    assert response.status_code == 400
    assert response.json() == {"price": ["Ensure this value is greater than or equal to 0."]}


@pytest.mark.django_db
def test_create_ad_incorrect_name(client, user, category):
    data = {
            "id": 1,
            "name": "name",
            "author": user.id,
            "price": 2500,
            "is_published": False,
            "description": None,
            "category": category.id}

    response = client.post(
        "/ad/create_ad/",
        data,
        content_type="application/json",

    )
    assert response.status_code == 400
    assert response.json() == {"name": ["Ensure this field has at least 10 characters."]}
