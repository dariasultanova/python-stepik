"""Программа генерирует заданное количество паролей и включает в себя умную настройку на длину пароля,
а также на то, какие символы требуется в него включить, а какие исключить."""

import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
exceptions = 'il1ILo0O'

chars = ''

pwd_quantity = int(input('Укажите количество паролей для генерации: '))
pwd_length = int(input('Укажите длину одного пароля: '))
pwd_digits = input('Включать ли цифры 0123456789? (да/нет) ')
pwd_uppercase = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (да/нет) ')
pwd_lowercase = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (да/нет) ')
pwd_punctuation = input('Включать ли символы !#$%&*+-=?@^_? (да/нет) ')
pwd_exceptions = input('Исключать ли неоднозначные символы il1ILo0O? (да/нет) ')

if pwd_digits == 'да':
    chars += digits
if pwd_uppercase == 'да':
    chars += uppercase_letters
if pwd_lowercase == 'да':
    chars += lowercase_letters
if pwd_punctuation == 'да':
    chars += punctuation
if pwd_exceptions == 'да':
    for c in exceptions:
        chars.replace(c, '')


def generate_password(length=pwd_length, chars=chars):
    for i in range(pwd_quantity):
        print(''.join(random.sample(chars, length)))


generate_password()