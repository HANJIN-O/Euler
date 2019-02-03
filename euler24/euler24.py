from copy import copy
import time


def permutation1(list, count):
    count = count - 1
    number = len(list)
    order = []
    list.sort()
    result = ''

    for i in range(number-1, 0, -1):
        if count / factorial(i) > 1:
            order.append(int(count / factorial(i)))
            count = (count % factorial(i))

    for ch in order:
        result += str(list[ch])
        list.remove(list[ch])
        list.sort()

    while list:
        result += str(list.pop())

    return result

def permutation2(list, count):
    number = len(list)
    order = []
    list.sort()
    result = ''

    for i in range(number-1, 0, -1):
        if count / factorial(i) > 1 and count % factorial(i) != 0:
            order.append(int(count / factorial(i))+1)
            count = (count % factorial(i))
        elif count / factorial(i) > 1 and count % factorial(i) == 0:
            order.append(int(count / factorial(i)))
            count = (count % factorial(i))

    for ch in order:
        result += str(list[ch-1])
        list.remove(list[ch-1])
        list.sort()

    while list:
        result += str(list.pop())


    return result



def factorial(num):
    value = 1
    for i in range(1, num+1):
        value *= i
    return value

list = []
for i in range(0, 10):
    list.append(i)

start = time.time()

print(permutation1(list, 1000000))


end = time.time()

list = []
for i in range(0, 10):
    list.append(i)

start1 = time.time()

print(permutation2(list, 1000000))

end1 = time.time()




print("Time : %s " % (end - start))
print("Time1 : %s " % (end1 - start1))


