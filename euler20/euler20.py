import time

start = time.time()

value = 1
result = 0
for i in range(1, 100+1):
    value *= i
for j in range(0, len(str(value))):
    result += int(str(value)[j])

print(value)
print(result)


end = time.time()


print("Time : %s" % (end - start))