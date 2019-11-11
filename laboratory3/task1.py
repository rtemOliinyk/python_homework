import string
import re

def check_letter_number(letter):
    return bool(re.match('^[1-9]\d*$', letter))

def get_text():
    text = input("Введіть строку - ")
    separator = input("Введіть роздільник - ")
    return str(text), separator

def get_letters(prompt):
    number = input(prompt)
    while not check_letter_number(number):
        number = input(prompt)
    return int(number)

def separate_words():
    text, separator = get_text()
    word_list = text.split(separator)
    return word_list

def check_letters(word_list):
    first_letter = get_letters('Введіть номер першої літери - ')
    last_letter = get_letters('Введіть номер останньої літери з кінця - ')
    result_list = []
    for word in word_list:
        while not len(word) >= first_letter + last_letter:
            first_letter = get_letters('Введіть номер першої літери - ')
            last_letter = get_letters('Введіть номер останньої літери з кінця - ')
    for word in word_list:
        if word[first_letter - 1].lower() == word[len(word) - last_letter].lower():
            result_list.append(word)
    return result_list

def print_result(result_list):
    for word in result_list:
        print(word)

print_result(check_letters(separate_words()))