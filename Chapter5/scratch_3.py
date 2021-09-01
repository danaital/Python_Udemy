# starterPokemonKanto = {"Bulbasaur": ("1", "Grass/Poison",
#                                      "There is a plant seed on its back right from the day it was born, the seed slowly grows larger"),
#                        "Charmander": ("4", "Fire",
#                                       "From the time it was born. a flame burns at the tip of its tail. Its life would end if the flames were go out"),
#                        "Squirtle": ("7", "Water",
#                                     "When it retracts its long neck into his shell, it squirts out water with vigorous force")}
# starterPokemonKanto["Pikachu"] = ("25", "Electric",
#                                   "It has small electric sacs on both his cheecks. If threatened it looses electric charges from the sacs")
# print(starterPokemonKanto)
# print(starterPokemonKanto.keys())
# print(starterPokemonKanto.values())
# # test = "abcd"
# # test[2]= "F"
# # print(test)
# string1 = "abc"
# string2 = string1.upper()
# print(string2)
#
# challenge 8
# locations = {0: "You are sitting in front of a computer learning Python",
#              1: "You are standing at the end of a road before a small brick building",
#              2: "You are at the top of a hill",
#              3: "You are inside a building, a well house for a small stream",
#              4: "You are in a valley beside a stream",
#              5: "You are in the forest"}
#
# exits = {0: {"Q": 0},
#          1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
#          2: {"N": 5, "Q": 0},
#          3: {"W": 1, "Q": 0},
#          4: {"N": 1, "W": 2, "Q": 0},
#          5: {"W": 2, "S": 1, "Q": 0} }
#
# vocabulary = { "QUIT":  "Q",
#                "NORTH": "N",
#                "SOUTH": "S",
#                "EAST":  "E",
#                "WEST":  "W"}
#
# # print(locations[0].split())
# # print(locations[3].split(","))
# # print(' '.join(locations[0].split()))
#
# loc = 1
# while True:
#     availableExits = ", ".join(exits[loc].keys())
#
#     print(locations[loc])
#
#     if loc == 0:
#         break
#
#     direction = input("Available exits are " + availableExits + " ").upper()
#     print()
#     # Parse the user input, using our vocabulary dictionary if necessary
#     if len(direction) > 1:   # more than one letter, so check vocab
#         words = direction.split()
#         for word in words:
#             if word in vocabulary:
#                 direction = vocabulary[word]
#                 break
#
#     if direction in exits[loc]:
#         loc = exits[loc][direction]
#     else:
#         print("You cannot go in that direction")
# starterPokemonJohto = {"Chikorita": (
#     "152", "Grass", "Its pleasantly aromatic leaves have the ability to check the humidity and temperature."),
#     "Cydaquill": ("155", "Fire",
#                   "It usually stays hunched over. If it is angry or surprised, it shoots flames out of its back."),
#     "Totodile": ("158", "Water",
#                  "It is small but rough and tough. It won't hesitate to take a bite out of anything that moves."),
#     "Pikachu": ("25", "Electric",
#                 "It has small electric sacs on both his cheecks. If threatened it looses electric charges from the sacs, TEST 123")
# }
# starterPokemons= starterPokemonKanto.copy()
# starterPokemons.update(starterPokemonJohto)
# print(starterPokemons)

# Challenge 9
# locations = {0: {"desc": "You are sitting in front of a computer learning Python",
#                  "exits": {},
#                  "namedExits": {}},
#              1: {"desc": "You are standing at the end of a road before a small brick building",
#                  "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
#                  "namedExits": {"2": 2, "3": 3, "5": 5, "4": 4}},
#              2: {"desc": "You are at the top of a hill",
#                  "exits": {"N": 5, "Q": 0},
#                  "namedExits": {"5": 5}},
#              3: {"desc": "You are inside a building, a well house for a small stream",
#                  "exits": {"W": 1, "Q": 0},
#                  "namedExits": {"1": 1}},
#              4: {"desc": "You are in a valley beside a stream",
#                  "exits": {"N": 1, "W": 2, "Q": 0},
#                  "namedExits": {"1": 1, "2": 2}},
#              5: {"desc": "You are in the forest",
#                  "exits": {"W": 2, "S": 1, "Q": 0},
#                  "namedExits": {"2": 2, "1": 1}}
#              }
#
# vocabulary = {"QUIT": "Q",
#               "NORTH": "N",
#               "SOUTH": "S",
#               "EAST": "E",
#               "WEST": "W",
#               "ROAD": "1",
#               "HILL": "2",
#               "BUILDING": "3",
#               "VALLEY": "4",
#               "FOREST": "5"}
#
# loc = 1
# while True:
#     availableExits = ", ".join(locations["exits"].keys())
#
#     print(locations[loc]["namedExits"])
#
#     if loc == 0:
#         break
#     else:
#         allExits = locations[loc]["exits"].copy()
#         allExits.update(locations[loc]["namedExits"])
#
#     direction = input("Available exits are " + availableExits).upper()
#     print()
#
#     # Parse the user input, using our vocabulary dictionary if necessary
#     if len(direction) > 1:  # more than 1 letter, so check vocab
#         words = direction.split()
#         for word in words:
#             if word in vocabulary:   # does it contain a word we know?
#                 direction = vocabulary[word]
#                 break
#
#     if direction in allExits:
#         loc = allExits[direction]
#     else:
#         print("You cannot go in that direction")
#
# set1 = {1,2,3}
# set2 = {1,4,5,7}
# print(set1 | set2)
# i = 8
# set3 = set({i})
# print(set3)
# dict1 = {"t":i}
# print(dict1)
# print(set2|set3)
#
#
# Challenge 10
str1= "This is really easy challenge"
vowels = frozenset("aeiou".split())
list1 = []
for char in str1:
    if (char not in vowels) and (char != " "):
        list1.append(char.lower())
list1.sort()
print(list1)

anotherOpt = frozenset("aeiou")
finalSet = set(str1).difference(vowels)
print(sorted(finalSet))
