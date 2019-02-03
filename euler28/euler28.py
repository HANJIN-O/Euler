import time




start = time.time()

tmp = 0
round = 1
result = 1
last = 0

while 1:
    a = 2 * round
    last = a ** 2 + 2 * a + 1
    tmp = 4 * a ** 2 + 2 * a + 4
    result += tmp
    round += 1
    if last == 1002001:
        break


print(result)

end = time.time()

print("Time : %s " % (end - start))