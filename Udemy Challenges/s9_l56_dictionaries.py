fruit = {"orange": "a sweet, orange, citrus fruit",
        "apple": "good for making cider",
        "mango": "a delicious fruit with a seed",
        "quenepas": "a perfect way to celebrate summer"}

#print(fruit)
#while True:
#    dict_key = input("Please enter a fruit: ")
#    if dict_key == "quit":
#        break
#    
# create description object from input, then print
#    if dict_key in fruit:
#        description = fruit.get(dict_key, "We Don't have a " +dict_key)
#    print(description)
#    
# print each element within fruit 10 times
#    for i in range(10):
#        for snack in fruit:
#            print(snack + " is " + fruit[snack])
#
# extract definition from dictionary using input and print
#    if dict_key in fruit:
#        print(fruit.get(dict_key))
#    
# return a statement if the input is not found in the dictionary
#    else:
#        print("we do not have "+dict_key)


# create a list then sort it       
#ordered_keys = list(fruit.keys())
#ordered_keys.sort()
# replace the two lines above with:
#ordered_kets = sorted(list(fruit.keys()))
#
# for each element, write the element then its definition
#for f in ordered_keys:
#    print(f + " - " + fruit[f])

# efficient interation through the dictionary, return objects
for key in fruit:
    print(fruit[key])

#difference in keys() vs values()
#print(fruit.keys())
#print(fruit.values())

#can you add values after creating the two new objects?
#fruit_keys = fruit.keys()
#print(fruit_keys)
#
#fruit["papaya"]="it grows everywhere"
#print(fruit_keys) #yes it updates the object
