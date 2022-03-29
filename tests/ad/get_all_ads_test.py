import pytest
from ads.serializers import AdSerializer
from tests.factory import AdFactory


@pytest.mark.django_db
def test_get_all_ads(client):
    ads = AdFactory.create_batch(3)

    response = client.get("/ad/ad/")
    ads_list = []
    for ad in ads:
        ads_list.append({
            "author": ad.author.first_name,
            'author_id': ad.author_id,
            'category_id': ad.category_id,
            "id": ad.id,
            "name": ad.name,
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published,
            "image": ad.image.url if ad.image else None
          })

    expected_response = {
        "items": ads_list,
        "total": 3,
        "num_pages": 1
    }
    assert response.status_code == 200
    assert response.json() == expected_response
