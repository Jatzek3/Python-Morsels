from math import sqrt
from decimal import *

def is_perfect_square(number):
    if number < 0:
        return False
    number = sqrt(number)
    print(number)
    if number == int(number):
        print("true")
        return True
    else:
        print("false")
        return False


