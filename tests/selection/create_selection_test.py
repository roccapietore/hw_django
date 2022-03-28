import pytest


@pytest.mark.django_db
def test_selection_create(client, token, user, ad):
    access_token, refresh_token = token

    expected_response = {
        "id": 1,
        "name": "selection",
        "owner": user.id,
        "items": [ad.id],
       }

    response = client.post(
        "/selection/create/",
        content_type="application/json",
        HTTP_AUTHORIZATION="Bearer " + refresh_token
    )

    assert response.status_code == 201
    assert response.json() == expected_response

