import re


def sum_numbers_in_string(input_string: str) -> int:
    """
    Находит все целые числа в строке и возвращает их сумму.
    
    Args:
        input_string: Строка, в которой нужно найти числа.
        
    Returns:
        Сумма всех найденных целых чисел.
    """
    numbers_list = []
    number = ""
    for letter in input_string:
        if letter.isdigit() or letter in '.':
            number += letter
        else:
            if number != "":
                numbers_list.append(int(float(number)))
                number = ""
            else:
                continue
    if number != "":
        numbers_list.append(int(float(number)))
    return sum(numbers_list)

def sum_numbers_in_string_regex(input_string: str) -> int:
    """
    Находит все целые числа в строке и возвращает их сумму.
    
    Args:
        input_string: Строка, в которой нужно найти числа.
        
    Returns:
        Сумма всех найденных целых чисел.
    """
    pattern = r'\d+(?:\.\d+)?'
    str_list = re.findall(pattern, input_string)
    numbers_list = [int(float(num)) for num in str_list]
    return sum(numbers_list)


# string_1 = "I have 10 apples and 5 oranges"
# print(sum_numbers_in_string(string_1))

# string_2 = "No numbers here"
# print(sum_numbers_in_string(string_2))

# string_3 = "123 and 456 make 579"
# print(sum_numbers_in_string(string_3))

# string_4 = "1a2b3c4d"
# print(sum_numbers_in_string(string_4))

# string_5 = "Price is $19.99 and $29.99"
# print(sum_numbers_in_string(string_5))

# string_1 = "I have 10 apples and 5 oranges"
# print(sum_numbers_in_string_regex(string_1))

# string_2 = "No numbers here"
# print(sum_numbers_in_string_regex(string_2))

# string_3 = "123 and 456 make 579"
# print(sum_numbers_in_string_regex(string_3))

# string_4 = "1a2b3c4d"
# print(sum_numbers_in_string_regex(string_4))

# string_5 = "Price is $19.99 and $29.99"
# print(sum_numbers_in_string_regex(string_5))
