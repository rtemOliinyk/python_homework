import re

def check_int(x):
    return bool(re.match('^\d+$', x))

def get_number(prompt):
    number = input(prompt)
    while not check_int(number):
        number = input(prompt)
    return int(number)

def count_sum():
    x = get_number("Введіть x: ")
    n = get_number("Введіть n: ")
    i = 1
    sum = 0
    for i in range(n):
        sum+=pow(x,i)
    return sum

print(count_sum())