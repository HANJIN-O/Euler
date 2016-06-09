def trinum(count):
    result = int((count * (count+1)) / 2)
    # print("%s trinum : %s" % (count, result) )
    return result

def factor_list(num):
    factor = []
    for i in range(1, int((num+1) / 2)):
        if num % i == 0:
            factor.append(i)
        else:
            continue
    factor.append(num)
    return factor

def factorization(num):
    prime = []
    divide = 2
    while num >= divide:
        if num % divide == 0:
            prime.append(divide)
            num = int(num / divide)
        else:
            divide += 1
    return prime

def countofprime(num):
    primelist = factorization(num)
    list = []
    num_of_factor = 1
    while primelist:
        factor = primelist[0]
        factorcount = primelist.count(factor)
        list.append([factor, factorcount])
        for i in range(0, factorcount):
            primelist.remove(factor)
    for i in range(0, len(list)):
        num_of_factor *= (int(list[i][1])+1)
    return num_of_factor

print(trinum())
# count = 1
# num_of_factor = 0
# while 1:
#     num_of_factor = countofprime(trinum(count))
#     if num_of_factor < 500:
#         print("the num of factor : %s YET" % num_of_factor)
#         count += 1
#     else:
#         print("the num of factor : %s and trinum : %s and count : %s " % (num_of_factor, trinum(count), count) )
#         break