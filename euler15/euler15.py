
def factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result

print(int(factorial(40)/(factorial(20)*factorial(20))))