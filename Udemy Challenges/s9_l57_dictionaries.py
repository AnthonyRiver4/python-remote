fruit = {"orange": "a sweet, orange, citrus fruit",
        "apple": "good for making cider",
        "mango": "a delicious fruit with a seed",
        "quenepas": "a perfect way to celebrate summer"}

# additional to the keys() and values() fuctions
# list() outputs the key and its value
#print(fruit.items())

# to convert to a tuple, simply use tuple()
#f_tuple = tuple(fruit.items())
#print(f_tuple)

#for snack in f_tuple:
#    item,description = snack
#    print(item + " is " + description)

# print tuple out as a dictionary
#print(dict(f_tuple))

# utilization of the join() fucntion in lists,strings
myList = ["a", "b", "c"]
newString = ''
# inefficient method to create a string from a list
#for c in myList:
#    newString += c + ", "
# preferable to use this method, join separates each
# list element with the "" is it called upon
newString = ", ".join(myList)
print(newString,'\n')
print("-"*20)

# video game map project
# create the list of locations 
locations = {0: "You are outside the game!",
             1: "You are standing on top of the mountain",
             2: "You are standing in the soft sands of the beach",
             3: "You are in the cave with screeching bats",
             4: "You are in the field, with the wind blowing strong",
             5: "You are standing in the road"}
exits = [{"Q": 0},
        {"W":4, "S":3, "Q":0},
        {"W":3, "Q":0},
        {"W":4, "E":2, "N":1, "S":5, "Q":0},
        {"N":1, "Q":0},
        {"W":4, "N":3, "Q":0}]

loc = 4 
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
    
    direction = input("Available exits are " + availableExits +" >> ").upper()
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction!")