import time

class Wordcount:
    dictionary = {0:0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3,
                  11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 9}

    def __init__(self):
        self.result = 0

    def count(self, number):
        if number < 20:
            self.result += self.dictionary[number]
        elif 20 <= number and number < 100:
            self.twenty_to_hundred(number)
        elif 100 <= number and number < 1000:
            self.hundred_to_thousand(number)
        elif number == 1000:
            self.result += 11


    def twenty_to_hundred(self, number):
        if str(number)[0] in ['2','3','8','9']:
            self.result += 6
        elif str(number)[0] in ['4','5']:
            self.result += 5
        elif str(number)[0] in ['6']:
            self.result += 7
        elif str(number)[0] in ['0']:
            pass
        self.count(int(str(number)[1]))


    def hundred_to_thousand(self, number):
        if str(number)[1:3] == '00':
            self.result += 7
            self.count(int(str(number)[0]))
        elif str(number)[1:3] != '00':
            self.result += 10
            self.count(int(str(number)[0]))
            number = str(number)[1:3]
            self.count(int(number))


t1 = time.time()
wordcount1 = Wordcount()
result = 0
for i in range(1, 1001):
    wordcount1.count(i)
    result += wordcount1.result
    wordcount1.result = 0
t2 = time.time()


print("result : %s " % result)
print("time : %s " % (t2-t1))

wordcount2 = Wordcount()
wordcount2.count(342)
wordcount3 = Wordcount()
wordcount3.count(115)
wordcount4 = Wordcount()
wordcount4.count(201)
print("wordcount2 : %s " % wordcount2.result)
print("wordcount3 : %s " % wordcount3.result)
print("wordcount4 : %s " % wordcount4.result)

