def hailstone_sequence(num):
    count = 0
    while num != 1:
        if num % 2 == 0:
            num = int(num / 2)
            count += 1
        else:
            num = (num*3)+1
            count += 1
    return count

num = 999999
count = 0
while num > 1:
    if count < hailstone_sequence(num):
        count = hailstone_sequence(num)
        print("num : %s and count : %s" % (num, count))
    num -= 2

