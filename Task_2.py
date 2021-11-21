#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Самостоятельно проработайте пример с оптимизацией хвостовых вызовов в Python. С помощью пакета timeit оцените
# скорость работы функций factorial и fib с использованием интроспекции стека и без использования интроспекции стека.
# Приведите полученные результаты в отчет


import timeit
import sys


class TailRecurseException:
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


def tail_call_optimized(g):
    def func(*args, **kwargs):
        f = sys._getframe()
        if f.f_back and f.f_back.f_back and f.f_back.f_back.f_code == f.f_code:
            raise TailRecurseException(args, kwargs)
        else:
            while True:
                try:
                    return g(*args, **kwargs)
                except TailRecurseException as e:
                    args = e.args
                    kwargs = e.kwargs

    func.__doc__ = g.__doc__
    return func


def factorial():
    @tail_call_optimized
    def introspection_stack(n):
        product = 1
        while n > 1:
            product *= n
            n -= 1

        return product

    def no_introspection_stack(n, acc=1):
        if n == 0:
            return acc

        return no_introspection_stack(n - 1, n * acc)

    return {'introspection_stack': introspection_stack, 'no_introspection_stack': no_introspection_stack}


def fib():
    @tail_call_optimized
    def introspection_stack(n):
        a, b = 0, 1

        while n > 0:
            a, b = b, a + b
            n -= 1

        return a

    def no_introspection_stack(i, current=0, nxt=1):
        if i == 0:
            return current

        else:
            return no_introspection_stack(i - 1, nxt, current + nxt)

    return {'introspection_stack': introspection_stack, 'no_introspection_stack': no_introspection_stack}


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
    x = 1000
    lim_x = 20

    print("\nfib[introspection_stack] - optimized: (microsecond)")
    print(filter_float(test(fib()['introspection_stack'], x, int(x / lim_x))))

    print("\nfib[no_introspection_stack]: (microsecond)")
    print(filter_float(test(fib()['no_introspection_stack'], x, int(x / lim_x))))

    print("\nfactorial[introspection_stack] - optimized: (microsecond)")
    print(filter_float(test(factorial()['introspection_stack'], x, int(x / lim_x))))

    print("\nfactorial[no_introspection_stack]: (microsecond)")
    print(filter_float(test(factorial()['no_introspection_stack'], x, int(x / lim_x))))
