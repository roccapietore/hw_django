import pytest


@pytest.mark.django_db
def test_get_one_ad(client, token, user, category, ad):
    access_token, refresh_token = token
    expected_response = {
        "id": ad.id,
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


@pytest.mark.django_db
def test_not_found_ad(client, token):
    access_token, refresh_token = token

    response = client.get(
        f"/ad/ad/300/",
        content_type="application/json",
        HTTP_AUTHORIZATION="Bearer " + access_token
    )

    assert response.status_code == 404
    assert {"detail": "Not found."}
