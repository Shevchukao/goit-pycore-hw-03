from datetime import (
    datetime as dtdt,
)  # import datetime class, from module datetime, gives it short alias dtdt


def get_days_from_today(date: str) -> int:  # definition function
    try:
        date = dtdt.strptime(
            date, "%Y-%m-%d"
        ).date()  # convert date string into date in format datetime.datetime
        date_now = dtdt.today().date()  # date today in format datetime.datetime
        delta_date_now = (
            date - date_now
        )  # difference date input and date_now in format datetime.timedelta
        return delta_date_now.days  # return int number in days
    except ValueError:
        print("Error: Date format not correct. Use fromat 'yyyy-mm-dd'")
        return None


input_date = input("Enter date in format 'yyyy-mm-dd': ")  # input date
print(get_days_from_today(input_date))  # function call
