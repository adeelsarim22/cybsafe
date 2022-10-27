from urllib import response
import pytest
from .models import Pokemon
from django.urls import reverse

@pytest.mark.django_db
def test_get_pokemons(client):
    """
    Test for get pokemon API
    """
    Pokemon.objects.create(
            id = 1,
            name = "bulbasaur",
            weight = 5,
            height = 3,
            base_experience = 6.7
    )
    url = reverse("list-pokemon")
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_create_pokemon(client):
    """
    Test for create pokemon API
    """
    url = reverse("create-pokemon", kwargs={"pokemon":1})
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_creating_existing_pokemon(client):
    """
    Test to check if we can create another pokemon with already existing id
    """
    url = reverse("create-pokemon", kwargs={"pokemon":1})
    response = client.get(url)
    response2 = client.get(url)
    assert response2.status_code == 400
    assert response2.data["error"] == "Pokemon already exists"

@pytest.mark.django_db
def test_creating_pokemon_invalid_id(client):
    """
    Test to check if we can create a pokemon with invalid id
    """
    url = reverse("create-pokemon", kwargs={"pokemon":"1jklasdf"})
    response = client.get(url)
    assert response.status_code == 404
    assert response.data["error"] == "Not Found"

@pytest.mark.django_db
def test_put_pokemon(client):
    """
    Test put method to update pokemon
    """
    Pokemon.objects.create(
            id = 1,
            name = "bulbasaur",
            weight = 5,
            height = 3,
            base_experience = 6.7
    )
    payload = {
        "name": "put-name",
        "weight": 23,
        "height": 12,
        "base_experience": 3.2,
    }
    url = reverse("update-pokemon", kwargs={"pk": "1"})
    response = client.put(url, data=payload, content_type="application/json",)
    assert response.data['name'] == payload['name']
    assert response.data['weight'] == payload['weight']
    assert response.data['height'] == payload['height']
    assert response.data['base_experience'] == payload['base_experience']
    assert response.status_code == 200

@pytest.mark.django_db
def test_put_pokemon_invalid_id(client):
    """
    Test put method to update pokemon with invalid id
    """
    Pokemon.objects.create(
            id = 1,
            name = "bulbasaur",
            weight = 5,
            height = 3,
            base_experience = 6.7
    )
    payload = {
        "name": "put-name",
        "weight": 23,
        "height": 12,
        "base_experience": 3.2,
    }
    url = reverse("update-pokemon", kwargs={"pk": "1789"})
    response = client.put(url, data=payload, content_type="application/json",)
    assert response.data['detail'] == "Not found."
    assert response.status_code == 404

@pytest.mark.django_db
def test_patch_pokemon(client):
    """
    Test patch method to update pokemon 
    """
    Pokemon.objects.create(
            id = 1,
            name = "bulbasaur",
            weight = 5,
            height = 3,
            base_experience = 6.7
    )
    payload = {
        "name": "put-name"
    }
    url = reverse("update-pokemon", kwargs={"pk": "1"})
    response = client.patch(url, data=payload, content_type="application/json",)
    assert response.data['name'] == payload['name']
    assert response.status_code == 200

@pytest.mark.django_db
def test_patch_pokemon_invalid_id(client):
    """
    Test patch method to update pokemon with invalid id
    """
    Pokemon.objects.create(
            id = 1,
            name = "bulbasaur",
            weight = 5,
            height = 3,
            base_experience = 6.7
    )
    payload = {
        "name": "put-name"
    }
    url = reverse("update-pokemon", kwargs={"pk": "1789"})
    response = client.patch(url, data=payload, content_type="application/json",)
    assert response.data['detail'] == "Not found."
    assert response.status_code == 404