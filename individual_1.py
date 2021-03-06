#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Число правильных скобочных структур длины 6 равно 5: ()()(), (())(), ()(()), ((())), (()()).
# Напишите рекурсивную программу генерации всех правильных скобочных структур длины 2n.
#
# Указание: Правильная скобочная структура минимальной длины «()». Структуры большей длины получаются из структур
# меньшей длины, двумя способами:
#   1) если меньшую структуру взять в скобки,
#   2) если две меньших структуры записать последовательно


def generate(n):
    result = set()
    if n == 0:
        result.add("")
    for i in range(1, n + 1, 1):
        for item in generate(n - i):
            result.add("(" * i + ")" * i + item)
            result.add("(" * i + item + ")" * i)
            result.add(item + "(" * i + ")" * i)

    return result


print(generate(3))
