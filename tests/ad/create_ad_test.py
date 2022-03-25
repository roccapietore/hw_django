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

    data = {"name": "namenamename",
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


