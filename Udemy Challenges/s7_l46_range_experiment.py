#print the range from 0 to 100, instancees of 2
o = range(0,100, 2)
print(o)

print("-"*50)
#print the range divided into instances of 5, multiplied by 2
p = o[::5]
print(p)

print("-"*50)
#print each value within the range
for i in p:
    print(i)

print("-"*50)
#create and print the tuple of values
l = list(p)
print(l)

print("-"*50)
#Print each value in the tuple
for i in l:
    print(i)
