"""
The function for detection anomalous words by length
"""
import string


def find_anomalous_words(text: str) -> list[str]:
    """
    Находит слова, длина которых отличается от средней длины слов в тексте 
    более чем на 2 символа.

    :param text: Входная строка.
    :return: Список аномальных слов.
    """
    if text == "":
        return []

    words_list = [word.strip(string.punctuation) for word in text.split()]
    sum_len = 0
    for word in words_list:
        sum_len += len(word)
    avg_len = sum_len / len(words_list)

    anomal_words_list = []
    for word in words_list:
        if len(word) <= avg_len - 2 or len(word) >= avg_len + 2:
            anomal_words_list.append(word)

    return anomal_words_list


# str_1 = "Python is great for data science"
# print(find_anomalous_words(str_1))

# str_2 = "Hello world"
# print(find_anomalous_words(str_2))

# str_3 = "A BB CCC DDDD EEEEE"
# print(find_anomalous_words(str_3))
