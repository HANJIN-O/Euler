def cycle(num):
    k = 1
    while 1:
        if (10 ** k) % num == 1:
            print("cylces of %s : %s " % (num, k))
            break
        k += 1
    return [num, k]

result = [0, 0]

for i in range(2, 1001):
    if i % 2 != 0 and i % 5 != 0:
        tmp = cycle(i)
        if tmp[1] > result[1]:
            result = tmp



print("number : %s,  period : %s" % (result[0], result[1]))