import random  # import random module


def get_numbers_ticket(
    min: int, max: int, quantity: int
) -> list:  # define function with three integer parameters
    unique_numbers = set()  # initialized empty set for unique elements
    if (
        (1 <= min < max) and (min < max <= 1000) and ((max - min) + 1 >= quantity)
    ):  # check conditions
        #  while loop that continues running until unique_numbers set contains required number of elements
        while len(unique_numbers) < quantity:
            # insert into set new random numbers
            unique_numbers.add(random.randint(min, max))
        return sorted(list(unique_numbers))  # return sorted list from set
    else:
        return list(unique_numbers)  # return empty list


# variable assignment call function with valid argument
lottery_numbers = get_numbers_ticket(10, 14, 6)
print("Ваші лотерейні числа:", lottery_numbers)  # output returned list
