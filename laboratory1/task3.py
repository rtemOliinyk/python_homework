import re

def check_int(x):
    return bool(re.match('^[-+]{0,1}\d*(.\d+){0,1}$', x))

def get_number(prompt):
    number = input(prompt)
    while not check_int(number):
        number = input(prompt)
    return float(number)

def calculate():
    x = get_number("Введіть x: ")
    if x < 3.2:
        y = pow(x,4) + 9
    else:
        y = 54 * pow(x, 4) / -5 * pow(x,2) + 7
    return round(y, 3)

print(calculate())