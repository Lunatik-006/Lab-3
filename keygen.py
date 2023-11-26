from random import sample, choice


def GetNumbers(code):  # Выделить все числа из строки символов
    numbers = []

    for i in code:
        try:
            int(i)
            numbers.append(i)
        except ValueError:
            None

    return int("".join(numbers))


def KeyGeneration(number):
    split_number = list(number)
    letters_list = "abcdefghijklmnopqrstuvwxyz"

    # Получить строку из расположенных в случайном порядке
    # 3 последних цифр введенного числа и 2 случайных букв
    first_part = "".join(
        sample(number[3:] + choice(letters_list) + choice(letters_list), 5)
    )

    # Получить строку из расположенных в случайном порядке
    # 3 первых цифр введенного числа и 2 случайных букв
    second_part = "".join(
        sample(number[:3] + choice(letters_list) + choice(letters_list), 5)
    )

    sum_of_numbers = GetNumbers(first_part) + GetNumbers(second_part)
    
    # При необходимости дополнить сумму чисел из первых двух частей ключа
    # незначащими нулями, получить 3 часть ключа
    third_part = "0" * (4 - len(str(sum_of_numbers))) + str(sum_of_numbers)

    return first_part + "-" + second_part + " " + third_part


print(KeyGeneration("123456"))
