import time


def primeFactors(num):
    pf = []
    result = []
    divide = 2
    while divide <= num:
        if num%divide==0:
            pf.append(divide)
            num/=divide
        else:
            divide+=1
    while pf:
        result.append([pf[0], pf.count(pf[0])])
        temp = pf[0]
        while temp in pf:
            pf.remove(temp)
    return result


start = time.time()



result = primeFactors(600851475143)
print("Prime factors of %i are %s" % (600851475143, result))
print("The answer is %s" % result[len(result)-1][0])


end =time.time()
print("time : %s" % (end - start))