from Laba3 import gauss_glav_el
import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate as my_func

with open('function.txt', 'r') as file:
    lines = file.readlines()

X = [float(x) for x in lines[0].strip().split()]
Y = [float(x) for x in lines[1].strip().split()]

x_arr = [1, 2, 2.5, 4]

def print_matrix(m, eps=1):
    for r in m:
        for elem in r:
            elem = f'{elem: .{eps}f}'
            print(f"{elem: ^6}", end=" ")
        print()

def spline(X,Y):
    n = len(X) - 1 #количество отрезков
    Q = [[0]*(4*n+1) for _ in range(4*n)] #заготавливаем матрицу неизвестных коэффициентов

    n_str = 0 #номер строки
    ix = 0 #индекс икса
    iS = 0 #индекс сплайна

    #Коэфициэнты первой и последней графиков в первой и последней точках равны y[i]
    #И Вторые производные в крайних точках равны нулю
    #3*n - 1 + i - начало коэффициэнтов последней функции
    for i in range(4): #цикл для формирования неизвестных коэффициентов
        Q[n_str][i] = X[ix] ** (3 - i)
        Q[n_str + 1][3 * n - 1 + i] = X[n] ** (3 - i)


    for i in range(2): #цикл для поиска вторых производных для крайних точек
        Q[-2][i] = (3 - i) * (2 - i) * X[ix] ** (1 - i)
        Q[-1][3*n - 1 + i] = (3 - i) * (2 - i) * X[n] ** (1 - i)

    Q[n_str][-1] = Y[0]
    Q[n_str + 1][-1] = Y[-1]

    n_str += 2 #первые две строчки заняты, поэтому надо сделать +2
    ix += 1 #завершена работа с первой точкой
    #Пишем значения при ai bi ci и di при x**3, x**2 ... функции iS
    while ix < (n):
        for i in range(0,4):
            Q[n_str][iS + i] = X[ix] ** (3 - i)
            Q[n_str + 1][iS + 4 + i] = X[ix] ** (3 - i)
            #Первая производная
            Q[n_str + 2][iS + i] = (3 - i) * X[ix] ** (2 - i)
            Q[n_str + 2][iS + 4 + i] = -(3 - i) * X[ix] ** (2 - i)
            #Вторая производная
        for i in range(2):
            Q[n_str + 3][iS + i] = (3 - i) * (2 - i) * X[ix] ** (1 - i)
            Q[n_str + 3][iS + 4 + i] = -(3 - i) * (2 - i) * X[ix] ** (1 - i)

        #Возращение первой точки, с которой работаем
        Q[n_str][-1] = Y[ix]
        Q[n_str+1][-1] = Y[ix]
        n_str += 4
        iS += 4
        ix += 1
    print('1.')
    print_matrix(Q)
    print('')
    Q_new, Q_K = gauss_glav_el(Q)
    print('2.')
    print_matrix(Q)
    return Q_K, Q

def value_X(X_arr,X,K):
    for i in range(len(X_arr)):
        start = -1
        for j in range(len(X) - 1):
            if X_arr[i] >= X[j] and X_arr[i] <= X[j+1]:
                start = j
        sums = 0
        if start == -1:
            print("X за пределами функции")
        else:
            for j in range(4):
                sums += K[4*start + j] * X_arr[i] ** (3 - j)



Q_K, Q = spline(X,Y)

print(Q_K)

print(x_arr, sep='\n')
value_X(x_arr,X,Q_K)

print(X)
print(Y)

#Построение графика
x_points = np.array(X)
y_points = np.array(Y)

tck = my_func.splrep(x_points, y_points)

x = np.linspace(X[0], X[-1], 1000)
y = my_func.splev(x, tck)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Метод сплайнов =)')

plt.plot(x, y, label=' График функции')
plt.scatter(X, Y, color='red', label='Узловые точки')
plt.legend()
plt.show()



