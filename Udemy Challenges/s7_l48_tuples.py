#creation of a tupple
welcome = "bienvenidos a mi casa", 1995 #creating tupple objects
dia = "Lunes", "Martes", 2018
print(welcome)
print(welcome[0])
print(dia)

#dia[0] = "Martes"  #This cannot be done, tupple is 
# an inmutable object.
dia = dia[0], "Martes", dia[1] #changing the value of a tupple object
print(dia)

 
#creation of a list
Badu = ["Tyrone", "Green", 1996]
print(Badu)
Badu[0] = "Baduism" #modify list object, mutable
print(Badu)

#unpacking the tupple
Album, lyric, year = Badu
print(Album)