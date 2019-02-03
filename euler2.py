def fibonacci(limit):
    fibonacci = [1, 2]
    n = 0
    while fibonacci[len(fibonacci)-1] < limit:
        fibonacci.append(fibonacci[len(fibonacci)-2]+fibonacci[len(fibonacci)-1])
    fibonacci.pop()
    return fibonacci

def delOddNum(list):
    temp = []
    for x in list:
        if x%2==1:
            temp.append(x)
    for y in temp:
        list.remove(y)
    return list

def sumOfAttributes(list):
    result = 0
    for x in list:
        result += x
    return result


print(sumOfAttributes(delOddNum(fibonacci(4000000))))
