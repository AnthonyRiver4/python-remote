# excerpt = open("/Users/antho/Desktop/excerpt.txt", 'r') #r stands for read only

# for line in excerpt:
#     if "the" in line.lower():
#         print(line, end='')

# excerpt.close()



# with open("excerpt.txt", 'r') as excerpt:
#     for line in excerpt:
#         if "THE" in line.upper():
#             print(line, end='')


#closer to file format, no extra spaces
# with open("excerpt.txt", 'r') as excerpt:
#     line = excerpt.readline()
#     while line:
#         print(line, end='')
#         line = excerpt.readline()


#returns a list of the text
with open("excerpt.txt", 'r') as excerpt:
    lines = excerpt.readlines()
print(lines)

for line in lines:
    print(line, end='')

print("-"*20)

for line in lines[::-1]:
    print(line, end='') #the end='' causes the \n to be ignored