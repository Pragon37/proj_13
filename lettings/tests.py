from django.urls import reverse, resolve
from lettings.models import Address, Letting
import pytest
from pytest_django.asserts import assertTemplateUsed


def test_lettings_url():
    """Test that the url for lettings is named lettings:index"""
    path = reverse("lettings:index")

    assert resolve(path).view_name == "lettings:index"


@pytest.mark.django_db
def test_letting_index_title(client):
    """Test letting page title"""
    path = reverse("lettings:index")
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<title>Lettings</title>"

    assertTemplateUsed(response, "lettings/index.html")
    assert expected_content in content


@pytest.mark.django_db
def test_profile_user_title(client):
    """Test letting page title"""
    testAddress = Address.objects.create(
        number=7217,
        street="Bedford Street",
        city="Brunswick",
        state="GA",
        zip_code=31525,
        country_iso_code="USA",
    )
    Letting.objects.create(
        title="Joshua Tree Green Haus /w Hot Tub", address=testAddress
    )
    path = reverse(
        "lettings:letting",
        kwargs={'letting_id': 1}
        )
    print("PATH PATH PATH = ", path)
    response = client.get(path)
    content = response.content.decode()
    expected_content = "Joshua Tree Green Haus /w Hot Tub"

    assertTemplateUsed(response, "lettings/letting.html")
    assert expected_content in content
