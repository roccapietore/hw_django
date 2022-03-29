import pytest

from selection.models import Selection


@pytest.mark.django_db
def test_selection_create(client, token, user, ad):
    access_token, refresh_token = token

    data = {
        "name": "selection",
        "owner": user.id,
        "items": [ad.id],
       }
    assert not Selection.objects.count()

    response = client.post(
        "/selection/create/", data,
        content_type="application/json",
        HTTP_AUTHORIZATION="Bearer " + access_token
    )

    new_selection = Selection.objects.last()

    assert response.status_code == 201
    assert response.data == {
        "id": new_selection.id,
        "name": "selection",
        "owner": user.id,
        "items": [ad.id]
    }

