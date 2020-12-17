Dec 17th 3:00-4:15pm(75min)

import math

#Question 1
def three_five ():
#Use for loop to find multiples of 3 or 5   
    multiples = []
    for i in range(100):
        if i %3 == 0 or i %5 == 0:
            multiples += [i]
#Add the numbers to the list, and find the sum   
    s = sum(multiples)

    return s

# print(three_five())

#Question 2
def fibonacci():
    fibo = []
#define the first two numbers of the fibo sequence
    even_fibo = [1, 2]
    first = 1
    second = 2

    stop = False
#while loop to create the sequence by adding up neighbouring numbers
    while stop == False:
        third = first + second
        fibo += [third]
        first = second
        second = third
#Stop the loop
        if third > 4000000:
            stop = True

#Find even valued terms in the sequence
    for num in fibo:
        if num %2 == 0:
            even_fibo += [num]
        
    s = sum(even_fibo)
    return s

# print(fibonacci())    

#Question 3
def prime():
#enter the number
    n = 600851475143
    maxPrime = -1

    while n % 2 == 0: 
        maxPrime = 2
        n >>= 1   
#Divide n with different numbers to find the prime
    for i in range(3, int(math.sqrt(n)) + 1, 2): 

        while n % i == 0: 
            maxPrime = i 
            n = n / i 

    if n > 2: 
        maxPrime = n 
    return int(maxPrime)

print(prime())
