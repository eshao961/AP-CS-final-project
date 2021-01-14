Work Session 1: Dec 17th 3:00-4:15pm(75min)

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



Work Session2: Jan 6th 3:00-4:15pm(75min)
                        
#Question 4
#function for multiplying all three digit numbers to find palindromes
def palindrome():
    i = 100
    j = 100
#create a list to contain the found palindromes
    pal_list = []
    while i < 1000:
        while j < 1000:
            num = i * j
            #use the helper function to determine if the number is a palindrome
            if isPalindrome(num) == True:
                #if the number is a palindrome, add to the list
                pal_list += [num]

            j += 1
        i += 1
#the biggest palindrome is the last in the list
    biggest = pal_list[-1]
    return biggest
    
#helper function of determining a palindrome number
def isPalindrome(num):
#turn the input number into a string
    n = str(num)
    length = len(n)
    result = True
#a palindrome is the same from front to middle and back to middle   
    for i in range(int(length/2)):
        if n[i] != n[-1-i]:
            result = False
        
    return result


Work Session 3: Jan10th 7:00-8:20pm (80min)
           
 #Question5
#Helper function for checking divisions
def smallest_multiples(num):
    variable=0
    n=num
#check if the number n can be evenly divided by numbers from 11 to 20
    for i in range(10):
        if n%(i+11)==0:
            variable=variable+1
    #if all ten numbers can be divided, return true
    if variable==10:
        return True
    else:
        return False

#main function for looping through all possible numbers
def is_smallest(num):
    List=[]
    product=1
#find the range of possible numbers by multiplying all numbers from 11 to 20
    for i in range(10):
        product=product*(i+11)
#use the product of 11 to 20 as the range of the loop
    for n in (product):
#Use helper function to check if the number can be evenly divided by numbers from 11 to 20
        if smallest_multiples(n)==True:
            #if it can be evenly divided by all numbers, add to the List
            List+=n
#find the smallest number in the list
    smallest=min(List)
    return smallest


Work Session 4:Jan14th 3:00pm-4:20pm (80min)
  #Question 6
#function for finding sum of squares
def sum1(num):
    sum_square=0
#Use for loop to add up the sum of squares
    for i in range(num):
        sum_square+=(i+1)**2
    return sum_square
#function for finding the square of sums
def sum2(num):
#equation for finding the sum of numbers
    sum=((1+num)*num)/2
#square the sum of numbers
    square_sum=(sum)**2
    return square_sum
#Finding the sum square difference 
difference=sum2(100)-sum1(100)
print(difference)


#Question 7
#helper function  for finding prime number 
def primenumber(n):
    count = 0
    for i in range(2, n):
        #the number is not a prime number if it can be evenly divided by numbers that are not 1
        if n%i == 0:
        #therefore it returns false the loop ends 
            return False
            break
        else:
        #count refcords the count of number that cannot be divided
            count += 1
#the number is  prime number if it cannot be divided by any number besides 1 and itself 
    if count == n-2:
        return True

#Function for finding the value of the given nth term  
def find_term(n):
    x = 0
    count = 0
#the loop ends when the given nth term is reached 
    while count != n:
        #use while loop to check if number is prime number starting from 1
        x += 1
        if primenumber(x) == True:
            count += 1
    print(x)
#call on the function to find the 10001th term number
find_term(10001)
