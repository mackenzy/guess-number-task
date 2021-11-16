"""Guess The Number Game
"""

import numpy as np

def random_predict(number: int = 1, range_limit_from: int = 1, range_limit_to: int = 100) -> int:
    """Guessing what number is passed 

    Args:
        number (int, optional): The number to guess. Defaults to 1.
        range_limit_from (int, optional): The lowest limit of the range of numbers to guess. Inclusive.
        range_limit_to (int, optional): The highest limit of the range of numbers to guess. Inclusive.
    Returns:
        int: number of attempts
    """
    count = 0
    upper_bound = range_limit_to + 1
    lower_bound = range_limit_from - 1
    supposed_number = int((upper_bound - lower_bound) / 2)

    while True:
        count += 1
        if number == supposed_number:
            break  
        
        if number > supposed_number: 
            lower_bound = supposed_number
            supposed_number += int((upper_bound - lower_bound) / 2)
        else: 
            upper_bound = supposed_number
            supposed_number -= int((upper_bound - lower_bound) / 2)
        
    return count


def score_game(random_predict) -> int:
    """The function to measure the average score for 1000 attempts 

    Args:
        random_predict ([type]): function to guess

    Returns:
        int: average attempts to guess
    """
    count_ls = []
    random_array = np.random.randint(1, 101, size=(1000))  # list of numbers to guess

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Your algorithm predicts the number in :{score} attempts on average")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
