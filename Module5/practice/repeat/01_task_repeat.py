# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

import random

def gen_list(size, of, to):
    digits = []
    for el in range(size):
        number = random.randint(of, to)
        digits.append(number)
    return digits

print(gen_list(5, -10, 10))
