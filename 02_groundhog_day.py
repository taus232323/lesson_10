# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.


import random

ENLIGHTENMENT_CARMA_LEVEL = 777
karma = 0

class IamGodError(Exception):
    pass

class DrunkError(Exception):
    pass

class CarCrashError(Exception):
    pass

class GluttonyError(Exception):
    pass

class DepressionError(Exception):
    pass

class SuicideError(Exception):
    pass

def one_day():
    dice = random.randint(1, 7)
    if random.randint(1, 13) == 1:
        error = random.choice([IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError])
        raise error
    return dice

while karma < ENLIGHTENMENT_CARMA_LEVEL:
    try:
        karma += one_day()
        if karma >= ENLIGHTENMENT_CARMA_LEVEL:
            break
    except (IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError) as exc:
        with open('log.txt', 'a') as log_file:
            log_file.write(f'Exception occurred: {type(exc).__name__}\n')


# https://goo.gl/JnsDqu
