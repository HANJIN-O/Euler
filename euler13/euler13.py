result = 0
list = []
with open("number.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        result += int(line)
result = str(result)
for ch in result:
    list.append(ch)
print(''.join(list[0:10]))