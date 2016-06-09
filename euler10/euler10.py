def factorization(num):
    factor = []
    divide = 2
    while divide <= num/2:
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
    if result == []:
        # print("%s is the prime factor" % num)
        return 1
    else:
        return 0


def prime_sieve(end):
    prime = []
    oddnumlist = [2]
    i = 3
    while i < (end + 1):
        oddnumlist.append(i)
        i += 2
    count = 2
    while count ** 2 < end:
        count += 1
    count -= 1

    s1 = set(oddnumlist)
    # print(count)
    for k in range(2, count+1):
        if isprimefactor(k):
            prime.append(k)
        else:
            continue
    # print("s1 before for loop = %s" % s1)
    for k in range(0, len(prime)):
        value = prime[k]
        s2 = []
        while value <= end:
            s2.append(value)
            value += prime[k]
        s2 = set(s2)
        # print("s2 = %s" % s2)
        s1 = s1 - s2
        # print("s1 = %s" % s1)

    prime = prime + list(s1)
    # print(s1)
    return prime



input = int(input())
primelist = prime_sieve(input)
result = 0
for num in primelist:
    result += num


print("%s is the result" % result)
