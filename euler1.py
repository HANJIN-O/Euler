def sumOfMultiples(num1, num2, limit):
    list = []
    result = 0
    multi = num1 * num2
    temp = num1
    while num1 < limit:
        list.append(num1)
        num1 += temp
    temp = num2
    while num2 < limit:
        list.append(num2)
        num2 += temp
    temp = multi
    while multi < limit:
        list.remove(multi)
        multi += temp
    for x in list:
        result += x
    return result



print(sumOfMultiples(3,5,1000))
