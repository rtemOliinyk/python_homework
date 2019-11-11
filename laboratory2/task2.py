import re

def check_int(x):
    return bool(re.match('^\d+$', x))

def get_number(prompt):
    number = input(prompt)
    while not check_int(number):
        number = input(prompt)
    return int(number)

def count_k():
    N = get_number("Введіть N: ")
    K = 1
    while (N >= pow(K, 2)):
        K = K + 1
    return K

print(count_k())