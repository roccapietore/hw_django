import pytest


@pytest.mark.django_db
def test_get_one_ad(client, token, user, category, ad):
    access_token, refresh_token = token
    expected_response = {
        "name": "namenamename",
        "author": user.id,
        "price": 2500,
        "is_published": False,
        "description": None,
        "category": category.id,
        "image": None
    }

    response = client.get(
        f"/ad/ad/{ad.id}/",
        content_type="application/json",
        HTTP_AUTHORIZATION="Bearer " + access_token
    )

    assert response.status_code == 200
    assert response.json() == expected_response


