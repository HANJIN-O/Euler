
biggest=0

with open("number", 'r') as f:
    lines = f.readlines()
    linenum = 1
    for line in lines:
        print(linenum)
        linenum += 1
        for i in range(0, 5):
            for j in range(1, 11):
                if biggest<=int(line[0+(i*j)])*int(line[1+(i*j)])*int(line[2+(i*j)])*int(line[3+(i*j)])*int(line[4+(i*j)]):
                    biggest=int(line[0+(i*j)])*int(line[1+(i*j)])*int(line[2+(i*j)])*int(line[3+(i*j)])*int(line[4+(i*j)])
                    print(biggest)

print(biggest)