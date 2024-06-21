from math import *
#from random import *
import timeit
a = 1.5
b = 3.14
exp = 0.001
def f(x):
    return x ** 2 - 5 * sin(x)
def f_1(x):
    return 2 * x - 5 * cos(x)
def f_2(x):
    return 2 + 5 * sin(x)
def phi(x):
    return sqrt(5 * sin(x))
def phi_1(x):
    return (sqrt(5) * cos(x)) / (2 * sqrt(sin(x)))
def malopolovin(a, b, f, exp):
    start = timeit.timeit()
    iteration = 1
    while True:
        iteration += 1
        if f(b) * f(a) < 0:
            x = (a + b) / 2
            if f(x) == 0:
                return x
            if f(x) * f(a) < 0:
                b = x
            elif f(x) * f(b) < 0:
                a = x
            if abs(b - a) < 2 * exp:
                x = (a + b) / 2
                break
    end = timeit.timeit()
    return x, f(x), iteration, abs(end - start)
print('Метод половинного деления:')
print(malopolovin(a, b, f, exp))
def hord(a, b, f, exp):
    start = timeit.timeit()
    x0 = a
    x = b
    iteration = 1
    if f(x) * f_2(x) > 0:
        x0 = a
        while True:
            x = x0 - ((b - x0) / (f(b) - f(x0))) * f(x0)
            if abs(x - x0) <= exp:
                break
            x0 = x
            iteration += 1
    elif f(x0) * f_2(x0) < 0:
        x0 = b
        while True:
            x = x0 - ((x0 - a) / (f(x0) - f(a))) * f(x0)
            if abs(x - x0) <= exp:
                break
            x0 = x
            iteration += 1
    end = timeit.timeit()
    return x, f(x), iteration, abs(end - start)
print('Метод хорд:')
print(hord(a, b, f, exp))
def newton(a, b, f, exp):
    start = timeit.timeit()
    iteration = 1
    x0 = 0
    if f(a)*f_2(a) > 0:
        x0 = a
    elif f(b)*f_2(b) > 0:
        x0 = b
    x1 = x0 - (f(x0) / f_1(x0))
    while True:
        x = x1 - f(x1)/f_1(x1)
        iteration += 1
        if abs(x - x1) <= exp:
            break
        x1 = x
    end = timeit.timeit()
    return x, f(x), iteration, abs(end - start)
print('Метод Ньютона:')
print(newton(a, b, f, exp))
# def method_iteration(x0, f, exp):
#     start = timeit.timeit()
#     x = x0
#     iteration = 1
#     # if abs(phi_1(x)) > 1:
#     #     print('Функция не сходима')
#     #     return None
#     while True:
#         iteration += 1
#         next_x = phi(x)
#         if abs(next_x - x) < exp:
#             break
#         x = next_x
#     end = timeit.timeit()
#     return x, f(x), iteration, abs(end - start)
# print(method_iteration((a + b) / 2, f, exp)) #uniform(a, b)
def method_iteration(a, b, f, exp):
    start = timeit.timeit()
    iteration = 1
    x0 = (a + b) / 2
    x = phi(x0)
    q = abs(phi_1(x0))
    if abs(q) > 1:
        raise Exception("Метод не работает, функция не сходится")
    while True:
        x0 = x
        x = phi(x0)
        iteration += 1
        if abs(x - x0) < ((1 - q) / q) * exp:
            break
    end = timeit.timeit()
    return x, f(x), iteration, abs(end - start)
print('Метод простых итераций:')
print(method_iteration(a, b, f, exp))
