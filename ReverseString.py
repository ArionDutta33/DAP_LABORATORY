def reverseString(string):
    result_string = list(string)   
    start, end = 0, len(result_string) - 1

    while start < end:
        result_string[start], result_string[end] = result_string[end], result_string[start]
        start += 1
        end -= 1

    return "".join(result_string)

print(reverseString("laravel"))  
