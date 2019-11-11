import re

def check_int(x):
    return bool(re.match('^[-+]{0,1}\d*(.\d+){0,1}$', x))

def get_number(prompt):
    number = input(prompt)
    while not check_int(number):
        number = input(prompt)
    return float(number)

def get_result():
    a = get_number("Введіть а: ")
    b = get_number("Введіть b: ")
    c = get_number("Введіть c: ")
    x = get_number("Введіть x: ")
    n = get_number("Введіть n: ")
    m = get_number("Введіть m: ")
    y = a * pow(x, 2) + b * x + c
    if (y == m) & (x == n):
        return "Графік пройде через точку (n,m)"
    else:
        return  "Графік не пройде через точку (n,m)"

print(get_result())