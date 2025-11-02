import random  # import random module


def get_numbers_ticket(
    min: int, max: int, quantity: int
) -> list:  # define function with three integer parameters
    unique_numbers = set()  # initialized empty set for unique elements
    if (min >= 1) and (max <= 1000):  # check conditions
        while (
            len(unique_numbers) < quantity
        ):  # while loop that continues running until unique_numbers set contains required number of elements
            unique_numbers.add(
                random.randint(min, max)
            )  # insert into set new random numbers
        return sorted(list(unique_numbers))  # return sorted list from set
    else:
        return list(unique_numbers)  # return empty list


lottery_numbers = get_numbers_ticket(
    1, 80, 10
)  # variable assignment call function with valid argument
print("Ваші лотерейні числа:", lottery_numbers)  # output returned list

