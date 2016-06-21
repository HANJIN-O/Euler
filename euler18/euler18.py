import time
# def sub(file, file2):
#     with open(file, 'r') as f:
#         lines = f.readlines()
#         f2 = open(file2, 'w')
#         for line in lines:
#             f2.write(line.replace(" ", ""))
#         f2.close()
#
# def find(file):
#
#     return
#
# def slice(file, file2):
#     number = []
#     with open(file, 'r') as f:
#         lines = f.readlines()
#         for line in lines:
#             i = 0
#             while i < len(line):
#                 number.append(line[i:i+2])
#                 i += 2
#         # number.sort()
#         while number.count('\n'):
#             number.remove('\n')
#         f2 = open(file2, 'w')
#         for i in range(0, len(number), 2):
#             f2.write(str(number[i]))
#             f2.write('\b')
#
# def frequency(file):
#     num = []
#     j = 0
#     frequency = []
#     with open(file, 'r') as f:
#         line = f.readline()
#         for i in range(0, len(line), 3):
#             num.append(line[i:i+2])
#
#     while j < len(num):
#         count = num.count(num[j])
#         frequency.append([num[j], count])
#         j += 1
#
#     print(frequency)
#
# def sort(file, file2):
#     list = []
#     with open(file, 'r') as f:
#         line = f.readline()
#         for i in range(0, len(line), 3):
#             list.append(line[i:i+2])
#     list.sort()
#
#     f2 = open(file2, 'w')
#     f2.write(str(list))
#
#     return list
#
# sub("text.txt", "text3.txt")
# slice("text3.txt", "text5.txt")
# sort("text5.txt", "text6.txt")
# frequency("text5.txt")



#### above this line
### my try which was fail


###  I got hint from here, actually solution :P
###
### http://radiusofcircle.blogspot.kr/2016/04/problem-18-project-euler-solution-with-python.html


# put number into list in type of integer
def makelist(file1):
    list = []
    f1 = open(file1, 'r')
    while True:
        line = f1.readline()
        if not line: break
        list.append(line.strip().split())
    f1.close()
    for i in range(0, len(list)):
        for j in range(0, len(list)-(14-i)):
            #convert to integer
            list[i][j] = int(list[i][j])


    return list

def calculate(list):
    result = 0
    ### len(list) is the height of number
    while len(list) != 1:
        for i in range(0, len(list[len(list)-2])):
            ###
            if list[len(list)-1][i] > list[len(list)-1][i+1]:
                list[len(list)-2][i] += list[len(list)-1][i]
            else:
                list[len(list)-2][i] += list[len(list)-1][i+1]
            ###
        del list[len(list)-1]

    result = list[0][0]
    return result


start = time.time()

list = makelist('text.txt')
print(calculate(list))

end = time.time()

print("time : %s" % (end - start))