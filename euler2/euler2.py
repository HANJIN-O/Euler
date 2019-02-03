sequence = [1, 2]

number = input("몇 이하의 숫자까지 피보나치 수열을 진행할 것인지 결정하시오 : ")

i = 0
sum = 2
print(sequence[i])
print(sequence[i+1])
while sequence[i]+sequence[i+1] < int(number):
    sequence.append(sequence[i] + sequence[i+1])
    print(sequence[i+2])
    if sequence[i+2]%2==0:
        sum+=sequence[i+2]
        print("sum : %d" % sum)
    i+=1


print("result : %d" % sum)

