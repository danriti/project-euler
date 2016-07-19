""" problem019.py

You are given the following information, but you may prefer to do some research
for yourself.

- 1 Jan 1900 was a Monday.
- Thirty days has September, April, June and November. All the rest have
  thirty-one, Saving February alone, Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but not on a century
  unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?

"""




DAYS_IN_MONTH = {
    1: 31, # jan
    2: 28, # feb
    3: 31, # mar
    4: 30, # april
    5: 31, # may
    6: 30, # june
    7: 31, # july
    8: 31, # aug
    9: 30, # sept
   10: 31, # oct
   11: 30, # nov
   12: 31  # dec
}

DAYS_OF_WEEK = [
   'monday',
   'tuesday',
   'wednesday',
   'thursday',
   'friday',
   'saturday',
   'sunday'
]

def main():
    start = 1900
    end = 2000
    day_offset = 0 # 1 Jan 1900 was a Monday, so start there
    any_given_sundays = []

    for year in xrange(start, end + 1):
        for month, days in DAYS_IN_MONTH.iteritems():
            for day in xrange(1, days+1):
                index = (day - 1 + day_offset) % 7

                if DAYS_OF_WEEK[index] == 'sunday' and day == 1 and \
                   year >= 1901:
                    any_given_sundays.append((year, month, day,))

            day_offset = index + 1

    print len(any_given_sundays)


if __name__ == '__main__':
    main()
