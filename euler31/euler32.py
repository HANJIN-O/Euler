import time


def gcd(a, b): # a is bigger
    if a < b:
        print("a must be bigger number")
        exit()
    elif a == b:
        return a
    else:
        if a % b != 0:
            while a % b != 0:
                print((a, b))
                c = a % b
                a = b
                b = c
            return b
        else:
            return a

def bcd(a, b): # a is bigger
    if a < b:
        print("a must be bigger number")
        exit()
    else:
        return a*b/gcd(a,b)

start = time.time()

list_of_coins = [1, 2, 5, 10, 20, 50, 100]

result = 8 #when u use only one sort of coin, there is just one way to make 200pence==2pound

for n in range(0, len(list_of_coins)+1):
    list_of_coins[0]

print(gcd(720, 128))

end = time.time()



print("Time : %s" % (end-start))