#creation of a tupple
welcome = "bienvenidos a mi casa", 1995 #creating tupple objects
dia = "Semana Santa", "Martes de Grasa", 2018, (
    (1, "Domingo"),(2, "Lunes"),(3, "Martes"),(4, "Miercoles"))

#creation of a list
Badu = ["Tyrone", "Green", 1996]
print(Badu)
Badu[0] = "Baduism" #modify list object, mutable
print(Badu)

#appending an element to the list, can ONLY be used with list items
Badu.append("Call you back")

#unpacking the list
print(Badu)

#unpacking the tupple
#the 4th group of elements will all store within dias
sem, fiesta, ano, dias = dia
print(fiesta)
print(dias)
