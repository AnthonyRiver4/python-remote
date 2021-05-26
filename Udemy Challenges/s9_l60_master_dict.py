# create the dictionary of locations: description, exits, namedExits
locations = {0: {"desc": "You are outside the game!",
                 "exits": {},
                 "namedExiits": {}},    
             1: {"desc": "You are standing on top of the mountain",
                 "exits": {"W":4, "S":3, "Q":0},
                 "namedExits": {"3": 3, "4": 4}},
             2: {"desc": "You are standing in the soft sands of the beach",
                 "exits": {"W":3, "Q":0},
                 "namedExits": {"3": 3}},
             3: {"desc": "You are in the cave with screeching bats",
                 "exits": {"W":4, "E":2, "N":1, "S":5, "Q":0},
                 "namedExits": {"1": 1, "2": 2, "4": 4, "5": 5}},
             4: {"desc": "You are in the field, with the wind blowing strong",
                 "exits": {"N":1, "Q":0},
                 "namedExits": {"1": 1}},
             5: {"desc": "You are standing in the road",
                 "exits": {"W":4, "N":3, "Q":0},
                 "namedExits": {"3": 3, "4": 4}}
             }


#create a new dictionary copying another
new_dict = locations.copy()

#create a dictinoary of command words the player might use to navigate
vocabulary = {"QUIT": "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST": "E",
              "WEST": "W",
              "MOUNTAIN": "1",
              "BEACH": "2",
              "CAVE": "3",
              "FIELD": "4",
              "ROAD": "5"}
              
loc = 4   #start at centralized location
while True:
# we are breaking rules by concatenating strings
#    availableExits = ""
#    for direction in exits[loc].keys():
#        availableExits += direction +", "
# The three lines above can be replaced with this:
    availableExits = ", ".join(exits[loc].keys())

    print(locations[loc])

    if loc==0:
        break
# create a copy of location values in exits    
    else:
        allExits = exits[loc].copy()
        allExits.update(namedExits[loc])
    
    direction = input("Available exits are " + availableExits +" >> ").upper()
    print()

# parse the user input for a match to vocabulary
    if len(direction) >1: # more than 1 letter
        for word in vocabulary: # is the word in our dictionnary
            if word in direction:
                direction = vocabulary[word]
                break


    if direction in allExits: #combination of exits and namedExits
        loc = allExits[direction]
    else:
        print("You cannot go in that direction!")