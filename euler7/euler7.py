def factorization(num):
    factor = []
    divide = 2
    while divide <= num:
        if num%divide == 0:
            factor.append(divide)
            num = num/divide
            if num == divide and divide == 1:
                break
        else:
            divide += 1
            continue

    return factor

def isprimefactor(num):
    result = factorization(num)
    if result == [num]:
        print("%s is the prime factor" % num)
        return 1
    else:
        return 0


count = 1
num = 2
while count < 10002:
    if isprimefactor(num):
        print(count)
        count += 1
        num += 1
    else:
        num += 1

