#Python HW #5 Basic Loops "Fizz Buzz"
#print numbers 1 - 100
#multiples of 3 print Fizz not number
#multiples of 5 print Buzz not number
#multiples of 3 and 5 print FizzBuzz
#prime numbers print Prime

#function to check if number is prime
def IsPrime(a):
    for count in range(2,a):
            if i%count == 0:
                return False
            if count == i-1:
                return True
                

i = 1
#iterate through 100
while i <= 100:
    #check if prime, print Prime if it is
    if IsPrime(i) == True:
        print("Prime")
        i +=1
    # check if divisible by 3 and 5, print FizzBuzz if is        
    elif i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
        i += 1
    #check if divisible by 3, print Fizz if it is    
    elif i%3 == 0:
        print("Fizz")
        i += 1
    #check if divisible by 5, print Buzz if it is    
    elif i%5 == 0:
        print("Buzz")
        i += 1
    #print number if not divisible by 3 or 5 and is not prime    
    else:
        print(i)
        i += 1
