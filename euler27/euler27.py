import time

def prime(num):
    list = []
    for i in range(1, int(num/2)+1):
        if num % i == 0:
            list.append(i)
    if len(list) == 1:
        return True
    else:
        return False

biggest = 0
start = time.time()

for a in range(999, -999, -1):
    result = []
    for b in range(999, -999, -1):
        result = []
        for n in range(0, abs(a)+1):
            if prime(n ** 2 + a * n + b):
                result.append(prime(n ** 2 + a * n + b))
                print("%s %s %s %s" % (a, b ,n, len(result)))
                if biggest < len(result):
                    biggest = len(result)
                    biggest1 = [a, b, n, len(result)]
            else:
                break


print("Result : %s" % biggest1)

end = time.time()

print("Time : %s " % (end - start))