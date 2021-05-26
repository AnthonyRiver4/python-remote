farm_animals = {"sheep", "cow", "hen"}
print(farm_animals)

for animal in farm_animals:
    print(animal)

print("="*40)

wild_animals = set({"chango", "iguana", "coqui", "tiburon"})
#you can create a set with or without the "set" function
#if you want to create an empty set, you must use "set" function
print(wild_animals)

for animal in wild_animals:
    print(animal)

farm_animals.add("caballo")
wild_animals.add("aguaviva")
print(farm_animals)
print(wild_animals)
#you see that the added elements are placed randomly, since sets are not ordered

empty_set = set()
empty_set.add("a")

even = set(range(0,40,2))
print(even)

#-----------------------------------------------------#
print("-"*40)
print("Unoins")
#unions

#print length of even's elements
print(len(even))

squares_tuple = {4, 6, 9, 16, 25}
squares = set(squares_tuple)
print(squares)
print(len(squares))

print("-"*40)
print("Union formed")
#union formed, combine both sets
print(even.union(squares))
print(len(even.union(squares)))

print("-"*40)
print("Intersection")
#intersection formed, set of elements shared by both sets
print(even.intersection(squares))

print("="*40)
print("Sorting")
#use sort when dealing with large sets of numbers
# setA - setB = setA(without elements from B)
print(sorted(even))
print(sorted(squares))

print("even minus squares")
print(sorted(even.difference(squares)))
print(sorted(even-squares))

print("-"*40)
print("Sets 2 and Challenge")
even.difference_update(squares)
#updates even set with the elements of squares set
print(sorted(even))

#symmetric difference of two sets
#all members of one set or the other but not both
print("-"*40)
print("Symmetric difference")

print("symmetric even minus squares")
print(sorted(even.symmetric_difference(squares)))

print("symmetric squares minus even")
print(sorted(squares.symmetric_difference(even)))

