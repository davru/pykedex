import sys, requests, json
from io import BytesIO
from PIL import Image   
from pycolors import *
from funcs import *


print( pycol.BOLD + pycol.HEADER + "Welcome to the pokedex, ask for a pokemon: " + pycol.ENDC, end="" )
pokemon = input()

while True:
    response = getPokemon(pokemon)

    if response.status_code == 404:
        print( "This pokemon name is not valid, try again: ", end="" )
        pokemon = input()
        continue
 
    data = response.json()

    imgr = requests.get(data["sprites"]["front_default"])
    img = Image.open(BytesIO(imgr.content))
    img.show()

    print( "\n" + pycol.BOLD + pycol.UNDERLINE + data["name"].capitalize() + pycol.ENDC + " (pokeapi ID: " + str(data["id"]) + ")" + "\n" +
           "Weight: " + str(data["weight"]) + "\n" +
           "Height: " + str(data["height"]) + "\n" +
           "Base experience: " + str(data["base_experience"]) )
    types = []
    for t in data["types"]:
        types.append(t["type"]["name"])
    print( "Types: " + ', '.join(types) + "\n")

    print( "Do you wanna ask for another pokemon? (Y/n) ", end="" )
    answer = input()
    if answer == 'n':
        break
    else:
        print( "Enter the pokemon name: ", end="" )
        pokemon = input()
