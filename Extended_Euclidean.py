""" This script will solve for the gcd of two numbers promted by the user and then display 
the factors to solve the linear Diophantine equation 
- writen by Lincoln D'Epagnier """

""" imports """
import numpy as np

""" Setup """
# we will solve in form ax + by = d so
# Prompt User for two intergers to get gcd  eg. gcd(50,35)
first = int(input("Enter first interger: "))
second = int(input("Enter Second interger: "))
factors = {} # maps a number in to its factors as matrix    eg. if gcd(50,35) factors[5] = (-2,3)


""" Start of alg """
# if the larger number is entered second swith the numbers 
if first < second: 
    y = second 
    second = first
    first = y

x = first
y = second

# keep track of the factors in a dict
factors[x] = np.array([1,0])
factors[y] = np.array([0,1])

print()
print('*** Performing Extended Euclidan algorithim ***********************')

""" Repeated steps of the algoritm
when the algorithm is finished we will se d = ax + by where y == 0 then we know the gcd is in x """
while y != 0:
    # shift positions 
    d = x
    x = y

    a = int(d/x)
    y = d%x 

    # enter factors of y
    print(f"{d} = {a}({x}), + 1({y})") # b will always be 1 as it is the remainder
    factors[y] = factors[d] - a*factors[x]

""" Final prints to display the Liner Diaphantie Form """
# gcd will be the val of x as y will be 0
print('*******************************************************************')
print(f'gcd({first},{second}) = {x}') 
print(f"{x} = {factors[x][0]}({first}) + {factors[x][1]}({second})")
print()
