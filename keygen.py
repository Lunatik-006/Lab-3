import random


def get_numbers(code):
    numbers = []

    for i in code:
        try:
            int(i)
            numbers.append(i)
        except ValueError:
            None

    return int("".join(numbers))


def keyGeneration(entered_number):
    letters_list = "abcdefghijklmnopqrstuvwxyz"

    first_set = (
        entered_number[3:] + random.choice(letters_list) + random.choice(letters_list)
    )
    first_part = "".join(random.sample(first_set, 5))

    second_set = (
        entered_number[:3] + random.choice(letters_list) + random.choice(letters_list)
    )
    second_part = "".join(random.sample(second_set, 5))

    sum_of_numbers = get_numbers(first_part) + get_numbers(second_part)
    third_part = "0" * (4 - len(str(sum_of_numbers))) + str(sum_of_numbers)

    return first_part + "-" + second_part + " " + third_part

