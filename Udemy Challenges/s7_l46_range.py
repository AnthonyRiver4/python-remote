#create an inmutable tuple of numbers from 0 to 100 in increments of 1
my_list = list(range(0,100, 1)) #ends at 99, n-1

even = list(range(0,10,2))
odd = list(range(1,10,2))

print(my_list)
print(even)
print(odd)

my_string = "abcdefghijklmnopqrstuvwxyz"
#indexing the character location in the string
print(my_string.index('a')+1)
#Calling a specific character location
print(my_string[2])

sevens = range(7,1000000,7)
#input request plus output string
x = int(input("Please enter a value less than 1 million: "))
#if the input is within the sevens tuple, then...
if x in sevens:
    print("{} is divisible by seven".format(x))

small_decimals = range(0,10)
my_range = small_decimals[::2]

#print an specified index value within my_range
print(my_range.index(4))

#for every value within my_range, print each one
for i in my_range:
    print(i)

#print 30 instances of a '-', useful for debugging
print("-"*50)

#using range in the for loop definition
for i in range(3,30,3):
    print(i)

#negative values in the range cause a reverse order
#
backstring="egaugnal lufrewop yrev a si nohtyP"
print(backstring[::-1])
