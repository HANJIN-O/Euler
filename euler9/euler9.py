for c in reversed(range(1, 998)):
    for a in range(1, 1001-c):
        for b in range(2, 1001-c):
            if (a ** 2) + (b ** 2) == (c ** 2) and a + b + c == 1000 and a < b < c:
                print("%s^2 + %s^2 = %s^2" % (a, b, c))


