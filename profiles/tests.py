from django.urls import reverse, resolve


def test_profiles_url():
    """Test that the url for profiles is named profiles:index"""
    path = reverse("profiles:profiles_index")

    assert resolve(path).view_name == "profiles:index"


# def test_oc_lettings_site_index_welcome_user(client):
#     """Test greetings message on the home page"""
#     path = reverse("index")
#     response = client.get(path)
#     content = response.content.decode()
#     expected_content = "<h1>Welcome to Holiday Homes</h1>"

#     assert expected_content in content


# def test_oc_lettings_site_index_title(client):
#     """Test home page title"""
#     path = reverse("index")
#     response = client.get(path)
#     content = response.content.decode()
#     expected_content = "<title>Holiday Homes</title>"

#     assert expected_content in content
