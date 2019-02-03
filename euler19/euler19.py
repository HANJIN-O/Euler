import time

class Calendar:

    def check_date(self, date):
        if date % 7 == 0:
            return 'Tuesday'
        elif date % 7 == 1:
            return 'Wedensday'
        elif date % 7 == 2:
            return 'Thirsday'
        elif date % 7 == 3:
            return 'Friday'
        elif date % 7 == 4:
            return 'Saturday'
        elif date % 7 == 5:
            return 'Sunday'
        elif date % 7 == 6:
            return 'Monday'


    def count_sunday_on_firstday(self, start, end):
        date = 0
        count = 0
        for year in range(start, end+1):
            for month in range(1, 12+1):
                if month in [1, 3, 5, 7 ,8 ,10, 12]:
                    date += 31
                elif month in [4, 6, 9, 11]:
                    date += 30
                else:
                    if self.leap_year(year):
                        date += 29
                    else:
                        date += 28
                if self.check_date(date+1) == 'Sunday':
                    count += 1

        return count

    def leap_year(self, year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                return False
            elif year % 4 == 0:
                return True


start = time.time()

c1 = Calendar()
print(c1.count_sunday_on_firstday(1901, 2000))

end = time.time()

print("time : %s " % (end-start))