from django.urls import reverse, resolve
from django.contrib.auth.models import User
from profiles.models import Profile
import pytest
from pytest_django.asserts import assertTemplateUsed


def test_profiles_url():
    """Test that the url for profiles is named profiles:index"""
    path = reverse("profiles:index")

    assert resolve(path).view_name == "profiles:index"


@pytest.mark.django_db
def test_profile_index_title(client):
    """Test profile page title"""
    path = reverse("profiles:index")
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<title>Profiles</title>"

    assertTemplateUsed(response, 'profiles/index.html')
    assert expected_content in content


@pytest.mark.django_db
def test_profile_user_title(client):
    """Test profile user page title"""
    testUser = User.objects.create(username="HeadlinesGazer")
    Profile.objects.create(user=testUser)
    path = reverse("profiles:profile", kwargs={"username": "HeadlinesGazer"})
    response = client.get(path)
    content = response.content.decode()
    expected_content = "HeadlinesGazer"

    assertTemplateUsed(response, 'profiles/profile.html')
    assert expected_content in content
