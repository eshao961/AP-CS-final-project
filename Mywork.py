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



Work Session 5: Jan17 8:00pm-8:45pm (45min)
           
#Question 8
#save the numbers as a string
s = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
#create a variable largest
largest=0
#create a loop to know where to start and where to stop
for i in range(0, len(s) - 13 + 1):
  product = 1
#loop around 13 numbers at a time
  for j in range(i, i + 13):
      #multiply all the numbers and save them as product 
    product *= int(s[j: j + 1])
#compare eacgh product with the product of the previous 13 numbers 
  if product > largest:
      #replace the variable largest with the largest product
      largest=product

#print the largest product
print (largest)


Work Session 6: Jan 20th 8:00pm-9:00pm(60min)
            
 #Question 9
#Set a biggest possible range for a, since a cannot be bigger than 1000 due to the equation
for a in range(1, 1000):
    #similarly, set a biggest possible range for b
        for b in range(1, 1000):
        
          #represent c with a and b 
            c = (1000 - a) - b
        
            # According to the instructions, each number must be smaller than the next
            if a < b < c:
            
                # check if the second equation is met
                if a**2 + b**2 == c**2:
                
                    # If all conditions above are met, the proeduct of a,b,c is calculated
                    print(a * b * c)
            
#Question 10
#helper function for finding prime numbers
def prime(num):
    #prime numbers cannot be even numbers
    if num > 2 and num % 2 == 0:
        return False
    #use loop to check if the number can be divided by any numbers smaller than its square root
    else:
        for i in range(3, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
    #if not it is a prime number
    return True

#function for adding up all prime numbers found using helper function
def add(num):
    list = 0
    #for numbers in range,if it is a prime number, then it is added to the list
    for i in range(2, num):
        if prime(i):
            list=list+i
#the list is the sum of all prie numbers    
    return list

# Print the sum of all primes below two million
print(add(2000000))


