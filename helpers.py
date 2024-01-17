import random
import string


def get_random_string_with_letters(length: int) -> str:
    """
    Method for generating random string
    :param: length: string's length
    :return: string with define lenhth
    """
    result = random.choices(string.ascii_lowercase + string.ascii_uppercase, k=length)
    return ''.join(result)
