"""Create lottery ticket numbers"""

import random

def get_numbers_ticket(min_number: int, max_number: int, quantity: int) -> list:
    """Returns list of ticket numbers

        min_number
            minimal possible number in the sequence (not less then 1)
        max_number
            manimal possible number in the sequence (not more then 1000)
        qunatity
            amount of munbers in the ticket (the value must be between min_number and max_number)
    """

    if (min_number < 1 or max_number > 1000 or (min_number > quantity or quantity > max_number)):
        return []
    return random.sample(range(min_number, max_number + 1), quantity)

print(get_numbers_ticket(1, 1000, 1000)) # e.g. [38, 1, 30, 28, 29, 27]
