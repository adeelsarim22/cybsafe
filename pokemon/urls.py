from django.contrib import admin
from django.urls import path, include
from .views import (
    CreatePokemon,
    UpdatePokemon,
    ListPokemon
)

urlpatterns = [
    path('list-pokemons/', ListPokemon.as_view(), name="list-pokemon"),
    path('create-pokemon/<str:pokemon>/', CreatePokemon.as_view(), name="create-pokemon"),
    path('update-pokemon/<int:pk>/', UpdatePokemon.as_view(), name="update-pokemon"),
]
