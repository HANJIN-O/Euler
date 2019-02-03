from copy import copy
import time

def find(n):
    list = []
    sum = 0
    for i in range(1, int(n/2)+1):
        if n % i == 0:
            list.append(i)
    for i in list:
        sum += i
    if sum == n:
        return 'perfect'
    elif sum < n:
        return 'deficient'
    elif sum > n:
        return 'abundant'

start = time.time()

i = 0
list = []
while 1:
    if i > 28123:
        break
    print("%s : %s" % (i, find(i)))
    if find(i) == 'abundant':
        list.append(i)

    i += 1
number = []
for i in range(1, 28124):
    number.append(i)
for i in range(0, len(list)):
    for j in range(i, len(list)):
        if list[i]+list[j] in number:
            number.remove(list[i]+list[j])

sum = 0
print(number)
for num in number:
    sum += num
print(sum)

end = time.time()

print("Time : %s " % (end - start))