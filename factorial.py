num = int(input("Enter the number: "))

i = 1
res = 1  
while i <= num:
    res *= i 
    i += 1

print(f"Factorial of {num} is {res}")
