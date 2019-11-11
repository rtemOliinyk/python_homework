import math
import re

def check_int(x):
    return bool(re.match('^\d+$', x))

def count_year(r, v):
    year = 2 * r * math.pi / v
    return year

def get_number(prompt):
    number = input(prompt)
    while not check_int(number):
        number = input(prompt)
    return int(number)

def year_compare():
    r1 = get_number("Введіть r1: ")
    v1 = get_number("Введіть v1: ")
    r2 = get_number("Введіть r2: ")
    v2 = get_number("Введіть v2: ")
    year1 = count_year(r1, v1)
    year2 = count_year(r2, v2)
    if year1 > year2:
        return "Рік на першій планеті довший"
    if year2 > year1:
        return "Рік на другій планеті довший"
    if year2 == year1:
        return "Роки на планетах однакові"
print(year_compare())