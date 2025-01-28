import math

def isPrime(number):
    if number <= 1:
        return False 
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False   
    return True  

num = int(input("Enter a number: "))
print(f"{num} is prime: {isPrime(num)}")
