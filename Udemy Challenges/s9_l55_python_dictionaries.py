fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit" }

#print the dictionary
#print(fruit)

#print a specified definition
#print(fruit["lemon"])

#add to the dictionary
fruit["mango"] = "tropical and sweet!"
print(fruit)
del fruit["mango"]
print(fruit)

#motorbike section, same line definitions
bike = {"make": "Honda", "model": "250 dream", "colour": "red", "engine_size": 250}
#print the specified definition
print(bike["engine_size"])

#enter word in terminal to find definition
while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    if dict_key in fruit:
        description = fruit.get(dict_key)
        print(description)
    else:
        print("we don't have a " +dict_key)

#Addy's code
#funny = {"clallalacllalaclala": "somthing that makes people laugh or giggle"}
#print(funny)

#Antonio's code
#nonsense = {}
#nonsense["calalalalalclalalaclalal"]="some thing fun to say"
#print(nonsense)
#