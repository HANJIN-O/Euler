input = int(input())


def sumofsquare(num):
    sum = 0
    for i in range(1, num+1):
        sum += (i ** 2)

    return sum

def squareofsum(num):
    sum = 0
    for i in range(1, num+1):
        sum += i

    square = (sum ** 2)

    return square

print("%s - %s = %s" % (squareofsum(input), sumofsquare(input), squareofsum(input) - sumofsquare(input)))