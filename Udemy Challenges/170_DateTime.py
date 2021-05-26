import time
#prints out original time and date for computers
print(time.gmtime(0))

print('-'*40)
#prints out local time and date as a tupple
print(time.localtime())

print('-'*40)
#prints out the number of seconds since 1970
print(time.time())

print('-'*40)
#or print out dates and time individually

time_here = time.localtime()


print(time_here)
print("year:", time_here[0], time_here.tm_year)
print("month:", time_here[1], time_here.tm_mon)
print("day:", time_here[2], time_here.tm_mday)