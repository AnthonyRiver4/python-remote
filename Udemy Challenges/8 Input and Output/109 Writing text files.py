# cities = ["Kinshasa", "San Juan", "Leoganne", "Lagos"]

# with open("cities.txt", 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file, flush=True) 
# #print has a flush function. Data is buffered to be displayed/trasferred/etc.
# #because these actinos are slower than memory movements
# #this buffer can grow with larger sets of data. In order to
# #flush the buffer, you close the file in order to free up
# #space on your device



# cities = []

# #this method shows hidden features lie new line \n character
# with open("cities.txt", 'r') as city_file:
#     for city in city_file:
#         cities.append(city.strip('\n')) #strip removes the new line character as it is read
#                                         #strip can only remove from the begginning or end

# print(cities)
# for city in cities:
#     print(city)



# #tuple created and written to a file as a string
# imelda = "More Mayhem", "Mayhem May", "2011", (
#     (1, "Pulling the rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish town waltz"))

# with open("imelda3.txt", 'w') as imelda_file:
#     print(imelda, file=imelda_file)


# #use of eval is not best solution to reading from a file that could be edited
# with open("imelda3.txt", 'r') as imelda_file:
#     contents= imelda_file.readline()

# imelda = eval(contents)

# print(imelda)
# title, artist, year, tracks = imelda
# print(title)
# print(artist)
# print(year)


