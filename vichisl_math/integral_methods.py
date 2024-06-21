import timeit
a = 0
b = 1
def shag(Integral, p):
    eps = 0.0001
    n = 10
    start = timeit.timeit()
    while True:
        f1 = Integral(f, b, a, n)
        f2 = Integral(f, b, a, 2 * n)
        if (1/(2 ** p - 1) * abs(f1 - f2)) < eps:
            break
        else:
            n *= 2
    end = timeit.timeit()
    return f2, 2 * n, abs(end - start)

def mind_prem(f, b, a, n):

    delta_x = (b - a) / n
    result = 0
    for i in range(1, n + 1):
        result += f(delta_x * (i - 1) + delta_x / 2)
    return result * delta_x

def f(x):
    return x ** 2

print('Методом центр прямоугольников:', shag(mind_prem, 1))


def prav_prem(f, b, a, n):
    delta_x = (b - a) / n
    result = 0
    for i in range(1, n + 1):
        result += f(i * delta_x)
    return result * delta_x

print('Методом правых прямоугольников:', shag(prav_prem, 1))
def lev_pram(f, b, a, n):
    delta_x = (b - a) / n
    result = 0
    for i in range(0, n):
        result += f(i * delta_x)
    return result * delta_x
print('Методом левых прямоугольников:', shag(lev_pram, 1))
def trapeze(f, b, a, n):
    delta_x = (b - a) / n
    result = 0
    for i in range(1, n):
        result += f(i * delta_x)
    return (result + (f(a) + f(b)) / 2) * delta_x
print('Методом трапеции:', shag(trapeze, 2))
def simpson(f, b, a, n):
    delta_x = (b - a) / n
    result_1 = 0
    result_2 = 0
    for i in range(1, n + 1, 2):
        result_1 += f(a + i * delta_x)
    for i in range(0, n + 1, 2):
        result_2 += f(a + i * delta_x)
    return 1/3 * delta_x * (f(a) - f(b) + 4 * result_1 + 2 * result_2 )
print('Методом Сипсона:', shag(simpson, 4))

def newton(f, b, a, n):
    delta_x = (b - a) / n
    result_1 = 0
    result_2 = 0
    result_3 = 0
    for i in range(0, n + 1, 3):
        result_1 += f(i * delta_x)
    for i in range(1, n + 1, 3):
        result_2 += f(i * delta_x)
    for i in range(2, n + 1, 3):
        result_3 += f(i * delta_x)
    return (3 * delta_x)/8 * (f(a) - f(b) + 3 * (result_1 + result_2) + 2 * result_3)
print('Методом Ньютона:', shag(newton, 4))