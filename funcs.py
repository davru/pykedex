import requests, math

def getPokemon(pokemon):
    return requests.get("http://pokeapi.co/api/v2/pokemon/"+pokemon)

def getEvolChain(id):
    url = "http://pokeapi.co/api/v2/pokemon-species/" + str(id)
    resp = requests.get(url)
    data = resp.json()
    evol = requests.get(data["evolution_chain"]["url"]).json()["chain"]
    evols = evol["species"]["name"].capitalize()
    while evol["evolves_to"]:
        evol = evol["evolves_to"][0]
        evols = evols + " -> " + evol["species"]["name"].capitalize()
    return evols


def getStrBar(stat, base):
    # ▓▓▓▓▓▓▓▓░░░░░░░ 
    num = math.ceil(base/20)
    stat = stat.capitalize()
    statStr = " - " + stat + "▓" * num + "░" * (10-num) + " " + str(base)
    return statStr


if __name__ == "__main__":
    print(getStrBar("speed", 90))
    #print(getPokemon("pikachu"))