from rest_framework import serializers
from .models import (
    Pokemon
)

class ListPokemonSerializer(serializers.ModelSerializer):
    """
    Serializer for listing pokemons present in database
    """

    class Meta:
        model = Pokemon
        fields = "__all__"


class UpdatePokemonSerializer(serializers.ModelSerializer):
    """
    Serializer for updating pokemons
    """

    class Meta:
        model = Pokemon
        exclude = ["id",]