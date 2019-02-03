import time
#
# number = 600851475143
# lst = []
# for i in range(2, int(math.ceil(number//2))):
#     if number % i == 0:
#         lst.append(i)
#         print(lst)
# lst2 = []
# for j in lst:
#     lst3 = []
#     for k in range(2, j//2):
#         if j % k == 0:
#             lst3.append(k)
#     if len(lst3) == 0:
#         lst2.append(j)
# lst2.reverse()
# print("lst = %s" % lst)
# print("lst2 = %s" % lst2)
# print("lst3 = %s" % lst3)

# import math
#
# number = 183
# lst = []
# for i in range(2, int(math.ceil(number//2))):
#     if number % i == 0:
#         lst.append(i)
#         print(lst)
# lst2 = []
# for j in lst:
#     lst3 = []
#     for k in range(2, j//2):
#         if j % k == 0:
#             lst3.append(k)
#     if len(lst3) == 0:
#         lst2.append(j)
# print(lst2[0])
def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

start = time.time()

print(prime_list(600851475143))

end = time.time()

print("Time : %s" % (end - start))