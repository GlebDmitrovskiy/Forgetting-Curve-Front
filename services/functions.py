import string
import random


def text_generator(length):
    text = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    return text

def digit_generator(length, start=1):
    digit = (random.randrange(start,length+1))
    return digit


