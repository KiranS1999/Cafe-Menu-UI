import math 

print(math.factorial(5))

from math import factorial

def factorial1(x):
    return print(math.factorial(x))


factorial1(14)    


#1. c is global. b and a are local to my_function, d is global
#2. global variable created and destroyed when module is called 
# local variables created and destroyed when fucntion called and destroyed 
#3.if c had a value of 1 there would be no print statement
#4. create print variable as a global one with no value or use an else statement
