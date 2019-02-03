import time

def d(n):
    list = []
    sum = 0
    for i in range(1, int(n/2)+1):
        if n % i == 0:
            list.append(i)
    for i in list:
        sum += i
    return sum

def amicable(n1):
    n2 = d(n1)
    if n2 > 10000 or n2 == n1:
        return False
    if n1==d(n2):
        return True

start = time.time()

list = []
for i in range(1, 10000+1):
    if amicable(i):
        list.append(i)

print(list)
sum = 0
for i in list:
    sum += i
print(sum)


end = time.time()

print("Time : %s " % (end - start))