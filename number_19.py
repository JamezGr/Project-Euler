# Counting Sundays
# Problem 19
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

import datetime
from dateutil.relativedelta import relativedelta

weekdays = {
    "Saturday": 5,
    "Sunday": 6,
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4
}


def count_weekdays():
    sunday_count = 0
    start_date = datetime.datetime(2000, 12, 31)
    end_date = datetime.datetime(1901, 1, 1)

    time_difference = relativedelta(start_date, end_date).years

    for year in xrange(0, time_difference + 1, 1):
        start_of_year = end_date + relativedelta(years=year)
        for month in xrange(0, 12):
            start_of_month = start_of_year + relativedelta(months=month)
            if start_of_month.weekday() == weekdays["Sunday"]:
                sunday_count += 1

    print("There were " + str(sunday_count) + " Sundays between 01/01/1901 and 31/12/2000")


if __name__ == "__main__":
    count_weekdays()
