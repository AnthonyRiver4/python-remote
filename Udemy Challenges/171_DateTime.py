#reaction game
import time 
#monotomic timer used: the time cannot go backwards.
from time import monotonic as my_timer
import random

input("Press enter to start")

#random number generated between 1 and 6 and assigns to time variable
wait_time = random.randint(1, 6)
#function now sleeps for the randomly assigned amount of time
time.sleep(wait_time)
#upon waking, it stores the current time into a variable
start_time = my_timer()
input("press enter to stop")

end_time = my_timer()

#formats the stored time into a more readable form
#https://docs.python.org/3/library/time.html?highlight=time#time.strftime
print("started at " +time.strftime("%X", time.localtime(start_time)))
print("ended at " + time.strftime("%X", time.localtime(end_time)))

print("Your reaction time was {} seconds".format(end_time - start_time))