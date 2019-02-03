import time


start = time.time()

list = []
for a in range(2, 101):
    for b in range(2, 101):
        if a ** b not in list:
            list.append(a ** b)
print(len(list))



end = time.time()


print("Time : %s " % (end - start))