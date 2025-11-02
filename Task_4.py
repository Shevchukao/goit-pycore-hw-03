from datetime import (
    datetime as dtdt,
    timedelta as td,
)  # import class datetime and timedelta from module datetime


users = [
    {"name": "John Doe", "birthday": "1985.11.08"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Anton Shevchuk", "birthday": "1998.11.03"},
]  # input list from dictionaries


def get_upcoming_birthdays(users: list) -> list:  # define function
    upcoming = []  # create emply list
    for user in users:  # iterates through each user dictionaries in list
        birthday = dtdt.strptime(
            user["birthday"], "%Y.%m.%d"
        ).date()  # parses user's birtday string into datetime.date
        today = dtdt.today().date()  # get current date in datetime.date format
        birthday_this_year = birthday.replace(
            year=today.year
        )  # replace in user's birthday year into current year (2025)
        if (
            birthday_this_year < today
        ):  # check the birthday for this year has alrefy passed
            birthday_this_year = birthday.replace(
                year=today.year + 1
            )  # if yes, it calculates the birthday for the next year
        days_until_birthday = (
            birthday_this_year - today
        ).days  # calculates difference between today date and the upcoming birthday
        if 0 <= days_until_birthday <= 7:  # check if birthday within the next 7 days
            if (
                birthday_this_year.weekday() >= 5
            ):  # checks if day of week is 5(Saturday) or 6(Sunday)
                birthday_this_year += td(
                    days=(7 - birthday_this_year.weekday())
                )  # if it's a weekend it shifts the date forward to the next Monday(Saturday + 2 days, Sunday + 1 day)
            upcoming.append(
                {
                    "name": user["name"],
                    "congratulation_date": birthday_this_year.strftime("%Y.%m.%d"),
                }  # add dictionary in new format into empty upcoming list
            )
    return upcoming  # return list with new dictionaries key-values


upcoming_birthdays = get_upcoming_birthdays(users)  # function call
print("Список привітань на цьому тижні:", upcoming_birthdays)  # print result
