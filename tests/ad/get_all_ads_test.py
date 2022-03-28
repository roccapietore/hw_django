import pytest
from ads.serializers import AdSerializer
from tests.factory import AdFactory


@pytest.mark.django_db
def test_get_all_ads(client):
    ads = AdFactory.create_batch(3)
    expected_response = {
        "items": AdSerializer(ads, many=True).data,
        "total": 3,
        "num_pages": 1
    }

    response = client.get("/ad/ad/")

    assert response.status_code == 200
    assert response.json() == expected_response
