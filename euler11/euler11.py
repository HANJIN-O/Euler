def horizontal(lines):
    biggest = 0
    for linenum in range(0, 20):
        order = 0
        while order <= 48:
            if biggest < int(lines[linenum][order:order+2])*int(lines[linenum][order+3:order+5])*int(lines[linenum][order+6:order+8])*int(lines[linenum][order+9:order+11]):
                biggest = int(lines[linenum][order:order+2])*int(lines[linenum][order+3:order+5])*int(lines[linenum][order+6:order+8])*int(lines[linenum][order+9:order+11])
                order += 3
                print("biggest in horizontal : %s" % biggest)
                print("coordinate in horizontal : [%s][%s]" % (linenum, order) )
                # print(order)
            else:
                order += 3
                continue

    return biggest

def vertical(lines):
    biggest = 0
    verticallinenum = 0

    while verticallinenum <= 56:
        for linenum in range(0, 17):
            if biggest < int(lines[linenum][verticallinenum:verticallinenum+2])*int(lines[linenum+1][verticallinenum:verticallinenum+2])*int(lines[linenum+2][verticallinenum:verticallinenum+2])*int(lines[linenum+3][verticallinenum:verticallinenum+2]):
                biggest = int(lines[linenum][verticallinenum:verticallinenum+2])*int(lines[linenum+1][verticallinenum:verticallinenum+2])*int(lines[linenum+2][verticallinenum:verticallinenum+2])*int(lines[linenum+3][verticallinenum:verticallinenum+2])
                print("biggest in vertical : %s " % biggest)
                print("coordinate in vertical : [%s][%s]" % (linenum, verticallinenum) )
            else:
                continue
        verticallinenum += 3

    return biggest

def diagonal(lines):
    biggest1 = 0
    biggest2 = 0
    # left up to right down
    for linecount in range(0, 17):
        for verticalcount in range(0, 48):
            if biggest1 < int(lines[linecount][verticalcount:verticalcount+2])*int(lines[linecount+1][verticalcount+3:verticalcount+5])*int(lines[linecount+2][verticalcount+6:verticalcount+8])*int(lines[linecount+3][verticalcount+9:verticalcount+11]):
                biggest1 = int(lines[linecount][verticalcount:verticalcount+2])*int(lines[linecount+1][verticalcount+3:verticalcount+5])*int(lines[linecount+2][verticalcount+6:verticalcount+8])*int(lines[linecount+3][verticalcount+9:verticalcount+11])
                print("biggest1 in diagonal left up to right down : %s" % biggest1)
                print("coordinate in diagonal left up to right down : [%s][%s]" % (linecount, verticalcount))

    # left down to right up
    for linecount in range(3, 20):
        for verticalcount in range(0, 48):
            if biggest2 < int(lines[linecount][verticalcount:verticalcount+2])*int(lines[linecount-1][verticalcount+3:verticalcount+5])*int(lines[linecount-2][verticalcount+6:verticalcount+8])*int(lines[linecount-3][verticalcount+9:verticalcount+11]):
                biggest2 = int(lines[linecount][verticalcount:verticalcount+2])*int(lines[linecount-1][verticalcount+3:verticalcount+5])*int(lines[linecount-2][verticalcount+6:verticalcount+8])*int(lines[linecount-3][verticalcount+9:verticalcount+11])
                print("biggest2 in diagonal left down to right up : %s" % biggest2)
                print("coordinate in diagonal left down to right up : [%s][%s]" % (linecount, verticalcount))

    print("biggest1 : %s" % biggest1)
    print("biggest2 : %s" % biggest2)

    if biggest1 >= biggest2:
        return biggest1
    elif biggest2 >= biggest1:
        return biggest2

with open("number.txt", 'r') as f:
    lines = f.readlines()

# print(lines[17][48:50])
# print(lines[18][51:53])
# print(lines[19][54:56])
# print(lines[20][57:59])


result = 0
value1 = horizontal(lines)
value2 = vertical(lines)
value3 = diagonal(lines)

print("value1 : %s " % value1)
print("value2 : %s " % value2)
print("value3 : %s " % value3)

print(result)