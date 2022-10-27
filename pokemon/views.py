from django.shortcuts import render
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from .models import (
    Pokemon
)
from .serializers import (
    UpdatePokemonSerializer,
    ListPokemonSerializer
)
# Create your views here.

BASE_URL = "https://pokeapi.co/api/v2/pokemon"

class CreatePokemon(APIView):
    """
    API to create Pokemon using 'pokeapi' and saving it in database
    """

    def get(self, request, pokemon):
        response = requests.get(BASE_URL+f"/{pokemon}")
        if response.status_code == 200:
            pokemon_obj = dict()
            pokemon_data = response.json()
            pokemon_obj["id"] = pokemon
            pokemon_obj["name"] = pokemon_data["name"]
            pokemon_obj["weight"] = pokemon_data["weight"]
            pokemon_obj["height"] = pokemon_data["height"]
            pokemon_obj["base_experience"] = pokemon_data["base_experience"]
            try:
                Pokemon.objects.create(**pokemon_obj)
                return Response(pokemon_obj, status=200)
            except Exception as e:
                return Response({"error": "Pokemon already exists"}, status=400)
        
        return Response({"error": response.text}, status=response.status_code)


class UpdatePokemon(UpdateAPIView):
    """
    API to update Pokemons present in our database
    """
    serializer_class = UpdatePokemonSerializer
    queryset = Pokemon.objects.all()


class ListPokemon(ListAPIView):
    """
    API to list pokemons present in database
    """
    serializer_class = ListPokemonSerializer
    queryset = Pokemon.objects.all()



