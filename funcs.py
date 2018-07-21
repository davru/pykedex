import requests, math

def getPokemon(pokemon):
    return requests.get("http://pokeapi.co/api/v2/pokemon/"+pokemon)

def getStrBar(stat, base):
    # ▓▓▓▓▓▓▓▓░░░░░░░ 
    num = math.ceil(base/20)
    stat = stat.capitalize()
    statStr = " - " + stat + "▓" * num + "░" * (10-num) + " " + str(base)
    return statStr


if __name__ == "__main__":
    print(getStrBar("speed", 90))
    #print(getPokemon("pikachu"))