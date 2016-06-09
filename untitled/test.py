#after factoriztion, if factors are just 1 and num, it's primefactor


# factorization
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


def findhavemultiplier(num):
    i=1
    while num>i**2:
        i += 1

    return (i - 1)


result = 1
afterFactorization = [[1]]
haveToMultiply = []
dic1 = {}
findmultiplier = 0
primefactorhavetofindmultiplier = []

# Flow
input = int(input())
findmultiplier=findhavemultiplier(input)
print("%s are numbers which are have to find multiplier" % findmultiplier)

for i in range (2, findmultiplier+1):
    if isprimefactor(i):
        primefactorhavetofindmultiplier.append(i)

for i in range (2, input+1):
    a = isprimefactor(i)
    if a:
        result *= i
    else:
        afterFactorization.append(factorization(i))

print(primefactorhavetofindmultiplier)
for k in range(0, len(primefactorhavetofindmultiplier)):
    biggest = 0
    for i in range(0, len(afterFactorization)):
        if biggest < afterFactorization[i].count(primefactorhavetofindmultiplier[k]):
            biggest = afterFactorization[i].count(primefactorhavetofindmultiplier[k])

    print(biggest)
    print(primefactorhavetofindmultiplier[k])
    result *= primefactorhavetofindmultiplier[k]**(biggest-1)


print(result)

# print("%s * %s" % (result, afterFactorization))