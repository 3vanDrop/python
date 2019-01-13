"""@calc_weekday.py

@Description:
    Calculate day of the week by a given date

@Author:
        -- 3van --
"""
from datetime import datetime

class Date(object):
    """ -- Date Class - Solution -- """

    def __init__(self, *date):
        if len(date) != 3:
            raise ValueError('Expecting Day, Month & Year  as argument')
        self.date = date

    def __call__(self):
        return self.year_day_count() + self.day_count()
    
    def weekday(self):
        return (self.year_day_count() + self.day_count())%7

    def year_day_count(self):
        year = self.date[2]
        base = 365*(year-1)
        return base + int(self.leap_years())

    def day_count(self):
        day, month, year = self.date
        days_per_month = (
            31, 28 + int(self.is_leap(year)),
            31, 30, 31, 30, 31, 31, 30, 31, 30, 31        
        )
        count = 0
        for m in [i for i in range(month-1)]:
            count += days_per_month[m]
        return count + day-1

    def leap_years(self):
        year = self.date[2]
        base_leap = float( year/4 )
        div_by_100 = float( year/100 )
        div_by_400 = float( year/400 )
    
        return base_leap - (div_by_100-div_by_400)

    def is_leap(self, year):
        if not (year%4)==0:
            return False
        if (year%100)==0 and not (year%400)==0:
            return False
        return True

class Weekday:
    def __init__(self, *date):
        self.days = {
            0:'Monday',
            1:'Tuesday',
            2:'Wednesday',
            3:'Thursday',
            4:'Friday',
            5:'Saturday',
            6:'Sunday'
        }
        self.date = Date(*date)

    def __call__(self):
        return self.days[ self.date.weekday() ]

if __name__ == '__main__':
    date = datetime.today()
    today = Weekday(date.day, date.month, date.year)
    print( 'Today is', today() )
