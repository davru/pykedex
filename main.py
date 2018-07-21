import sys
from pycolors import *
from funcs import *


print( pycol.BOLD + pycol.HEADER + "Welcome to the pokedex, ask for a pokemon: " + pycol.ENDC, end="" )
pokemon = input()
valid = True

while True:
    valid = validatePokemon(pokemon)

    if not valid:
        print( "This pokemon name is not valid, try again: ", end="" )
        pokemon = input()
        continue

    print( "El pokemon " + pokemon + " es muy bonito!" )

    print( "Do you wanna ask for another pokemon? (Y/n) ", end="" )
    answer = input()
    if answer == 'n':
        break
    else:
        print( "Enter the pokemon name: ", end="" )
        pokemon = input()
