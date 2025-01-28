def count_case(s):
    upper_count = 0
    lower_count = 0
    
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    
    return upper_count, lower_count

string = input("Enter a string: ")
upper, lower = count_case(string)

print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")
