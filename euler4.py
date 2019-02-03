import time

def findPalindrone(digit):
    low = 10**(digit-1)
    high = (10**digit)-1
    palindrone = []
    for x in range(high, low-1, -1):
        for y in range(high, low-1, -1):
            multiple = str(x*y)
            if len(multiple)%2==0 and multiple[0:digit]==multiple[digit:][::-1]:
                palindrone.append(multiple)
    if len(palindrone)==0:
        for x in range(high, low - 1, -1):
             for y in range(high, low - 1, -1):
                multiple = str(x * y)
                if len(multiple)%2==1 and multiple[0:digit-1]==multiple[digit:][::-1] and len(palindrone)==0:
                    palindrone.append(multiple)
    palindrone = [int(x) for x in palindrone]
    palindrone.sort()
    palindrone.reverse()
    return palindrone
start = time.time()

print(findPalindrone(3)[0])

end = time.time()
print("Time : %s" % (end - start))
#
# import time
#
# start = time.time()
#
# lst = []
# for i in range(101, 1000):
#     for j in range(101, 1000):
#         number = i * j
#         string = str(number)
#         if len(string) == 5:
#             if (string[0] == string[-1]) and (string[1] == string[-2]):
#                 lst.append(number)
#         elif len(string) == 6:
#             if (string[0] == string[-1]) and (string[1] == string[-2]) \
#                     and (string[2] == string[-3]):
#                 lst.append(number)
#
# print(max(lst))
#
# end = time.time()
# print(end - start)