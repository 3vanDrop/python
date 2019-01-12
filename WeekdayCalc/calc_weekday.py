"""@calc_weekday.py

@Description:
    Calculate day of the week by a given date

@Author:
        -- 3van --
"""


from datetime import datetime

class Day(object):

    def __init__(self, *date):
        if len(date) != 3:
            raise ValueError('Expecting Day, Month & Year  as argument')
        self.days = {
            0:'Monday',
            1:'Tuesday',
            2:'Wednesday',
            3:'Thursday',
            4:'Friday',
            5:'Saturday',
            6:'Sunday'
        }
        self.date = datetime(*reversed(date))

    def weekday(self, *date):
        return self.days[ self.date.weekday() ]

if __name__ == '__main__':
    day = Day(12, 1, 2019)
