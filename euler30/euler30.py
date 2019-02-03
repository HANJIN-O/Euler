import time



start = time.time()

num = 2
result = 0
while 1:
    length = len(str(num))
    sum = 0
    for n in str(num):
        sum += int(n) ** 5
    if num == sum:
        print(num)
        result += num
    num += 1
    if num > 6 * (9**5):
        break

print("Result : %s" % result)

end = time.time()


print("Time : %s" % (end - start))