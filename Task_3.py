import re  # import regexp module


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]  # list with numbers in some format


def normalize_phone(num):  # define function
    pat1 = r"[^\d\+]+"  # regexp not a digit and not a plus, one and more
    num = re.sub(pat1, "", num)  # delete symbols
    if num.startswith("0"):  # if string start with 0
        num = "+38" + num  # concatenation "+38" and num
    elif num.startswith("38"):  # if string start with 38
        num = "+" + num  # concatenation "+" and num
    else:  # if string start with +38
        num  # not change string
    return num  # return result string


sanitized_numbers = [normalize_phone(num) for num in raw_numbers]  # list comprehension
print(
    "Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers
)  # prints phone number
