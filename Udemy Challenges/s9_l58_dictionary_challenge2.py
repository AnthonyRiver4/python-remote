# video game map project
# create the dictionary of locations 
locations = {0: "You are outside the game!",
             1: "You are standing on top of the mountain",
             2: "You are standing in the soft sands of the beach",
             3: "You are in the cave with screeching bats",
             4: "You are in the field, with the wind blowing strong",
             #5: "You are standing in the road
             }

#update dictionary with another
new = {5: "You are standing in the road"}
locations.update(new)

#create a new dictionary copying another
new_dict = locations.copy()

# create the dictionary of exits
exits = {0: {"Q": 0},
        1: {"W":4, "S":3, "Q":0},
        2: {"W":3, "Q":0},
        3: {"W":4, "E":2, "N":1, "S":5, "Q":0},
        4: {"N":1, "Q":0},
        5: {"W":4, "N":3, "Q":0}}

#create a dictionary of numbered exits
namedExits = {1: {"3": 3, "4": 4},
              2: {"3": 3},
              3: {"1": 1, "2": 2, "4": 4, "5": 5},
              4: {"1": 1},
              5: {"3": 3, "4": 4}}

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