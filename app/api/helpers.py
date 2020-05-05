import random
import string


def get_random_string(chars=22):
    char_set = f'{string.digits}{string.ascii_letters}'
    random.choice(char_set)
    return ''.join(random.sample(char_set, chars))