#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Самостоятельно изучите работу со стандартным пакетом Python timeit . Оцените с помощью этого модуля скорость
# работы итеративной и рекурсивной версий функций factorial и fib . Во сколько раз измениться скорость работы
# рекурсивных версий функций factorial и fib при использовании декоратора lru_cache ? Приведите в отчет и обоснуйте
# полученные результаты

from functools import lru_cache
import timeit


def fib():
    def iterative(n):
        a, b = 0, 1

        while n > 0:
            a, b = b, a + b
            n -= 1

        return a

    @lru_cache
    def recursive(n):
        if n == 0 or n == 1:
            return n

        else:
            return recursive(n - 2) + recursive(n - 1)

    return {'iterative': iterative, 'recursive': recursive}


def factorial():
    def iterative(n):
        product = 1
        while n > 1:
            product *= n
            n -= 1

        return product

    @lru_cache
    def recursive(n):
        if n == 0:
            return 1

        elif n == 1:
            return 1

        else:
            return n * recursive(n - 1)

    return {'iterative': iterative, 'recursive': recursive}


def test(fun, end, step, start=0):
    arr = []
    for i in range(start, end, step):
        start_timer = timeit.default_timer()
        fun(i)
        arr.append(timeit.default_timer() - start_timer)

    return arr


def filter_float(list_timer, timer=1000000):
    s = []
    for item_timer in list_timer:
        s.append(float(f"{(item_timer * timer):0.2f}"))

    return s


if __name__ == '__main__':
    x = 10000
    lim_x = 20

    print("\nfib[iterative]: (microsecond)")
    print(filter_float(test(fib()['iterative'], x, int(x/lim_x))))

    print("\nfib[recursive]: (microsecond)")
    print(filter_float(test(fib()['recursive'], x, int(x/lim_x))))

    print("\nfactorial[iterative]: (microsecond)")
    print(filter_float(test(factorial()['iterative'], x, int(x/lim_x))))

    print("\nfactorial[recursive]: (microsecond)")
    print(filter_float(test(factorial()['recursive'], x, int(x/lim_x))))
