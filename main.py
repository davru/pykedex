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


    #############################################################
    ########################### IMAGE ###########################
    #############################################################
    #imgburl = "https://assets.pokemon.com/assets/cms2/img/pokedex/full/" + str(data["id"]) + ".png"
    imgburl = "https://img.pokemondb.net/artwork/" + str(data["name"]) + ".jpg"
    imgr = requests.get(imgburl)
    img = Image.open(BytesIO(imgr.content))
    w, h = img.size
    img.resize((w, h)).show()


    #############################################################
    ######################### BASE INFO #########################
    #############################################################
    print( "\n" + pycol.BOLD + pycol.UNDERLINE + data["name"].capitalize() + pycol.ENDC + " (ID: " + str(data["id"]) + ")" + "\n" +
           "Weight: " + str(data["weight"]/10) + "kg\n" +
           "Height: " + str(data["height"]/10) + "m\n" +
           "Base experience: " + str(data["base_experience"]) )
    ########################### TYPES ###########################
    types, abilities = [], []
    for t in data["types"]:
        types.append(t["type"]["name"])
    print( "Types: " + ', '.join(types) )
    ######################### ABILITIES #########################
    for a in data["abilities"]:
        ab = a["ability"]["name"]
        if a["is_hidden"]:
            ab = ab + " (hidden ab.)"
        abilities.append(ab)
    print( "Abilities: " )
    for ab in abilities:
        print( " - " + ab.capitalize() )
    ########################### STATS ###########################
    print( "Stats: " )
    for s in data["stats"]:
        print(getStrBar((s["stat"]["name"] + ":").ljust(17), s["base_stat"]))
    ######################## EVOL CHAIN #########################
    print("Evolutions:\n" + " " + getEvolChain(data["id"]))
    print()
    #############################################################



    #############################################################
    ######################## END OF LOOP ########################
    #############################################################
    print( "Do you wanna ask for another pokemon? (Y/n) ", end="" )
    answer = input()
    if answer == 'n':
        break
    else:
        print( "Enter the pokemon name: ", end="" )
        pokemon = input()
