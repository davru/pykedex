import requests

def getPokemon(pokemon):
    return requests.get("http://pokeapi.co/api/v2/pokemon/"+pokemon)