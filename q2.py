# 2. Write a python program to create a function that takes a number as a parameter and
# checks if the number is prime or not.

def checkPrime(n):
    i=2
    while(i<=n**0.5):
        if(n%i==0):
            return 0
        i+=1
    else:  
        if(n==1):
            return 0  
        return 1


    
print("Prime number" if(checkPrime(int(input("Enter a number: ")))==1) else "Not a prime number")   
