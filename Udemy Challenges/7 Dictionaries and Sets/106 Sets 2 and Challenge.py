even = set(range(0, 40 , 2))
print(even)
squares_tuple = (4,6,9,16,25)
squares = set(squares_tuple)
print(squares)

squares.discard(4)
squares.remove(16) #can only be called if the element exists in the set
squares.discard(8)
print(squares)
try:
    squares.remove(8)
except KeyError:
    print("The item 8 is not a member is this set")

if squares.issubset(even):
    print("squares is a subset of even")

if even.issuperset(squares):
    print("even is a superset of squares")


even = frozenset(range(0,100,2)) #inmutable set

#----------------Challenge begins!--------------------------
