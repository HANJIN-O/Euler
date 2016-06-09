def wordcount(num):
    result = 0
    num = str(num)

    if len(num) == 1:
        result += underten(int(num))
    elif len(num) == 2:

    elif len(num) == 3:


    elif len(num) == 4:
        result += 11

    return result

def underten(num):
    result = 0
    if num in [1, 2, 6]:
        result += 3
    elif num in [4, 5, 9]:
        result += 4
    else:
        result += 5
    return result
def underhundred(num):
    result = 0

    return result
def underthousand(num):
    result = 0

    return result

wordcount(51)