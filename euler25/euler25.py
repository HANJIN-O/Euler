import time

def fibonacci(index):
    list = [1, 1]
    for i in range(2, index+1):
        list.append(list[i-2] + list[i-1])
    return list[index-1]

start = time.time()

# index = 0
# while 1:
#     if len(str(fibonacci(index))) == 1000:
#         break
#     index += 1

print(fibonacci(50))

end = time.time()


print("Time : %s " % (end - start))