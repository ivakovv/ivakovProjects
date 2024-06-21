# with open('matrix.txt', 'r') as file:
#     lines = file.readlines()

# A = []
# B = []
#
# for line in lines:
#     numbers = [float(x) for x in line.strip().split()]
#     A.append(numbers[:-1])
#     B.append(numbers[-1])


# A = [[1.15,0.42,100.71],
#      [1.10,0.55,0.32],
#      [1.00,0.35,3.00]]
#
# B = [-198.70, 2.29, -0.65]
# ответ 2,1,-2 (Верный ответ -2.031965739236835, -18.486411532883913, 11.916141254219893)
# A = [
#     [3.1,1.5,1.0],
#     [1.5,2.5,0.5],
#     [1.0,0.5,4.2],
# ]
#
# B = [10.83,9.20,17.10]
# ответ 1.3, 2.2, 3.5

# A = [
#     [2.0, 1.0, -0.1, 1.0],
#     [0.4, 0.5, 4.0, -8.5],
#     [0.3, -1.0, 1.0, 5.2],
#     [1.0, 0.2, 2.5, -1.0]
# ]
#
# B = [2.7, 21.9, -3.9, 9.9]
# -1, 3, 2 ,1
#Совмещение Матриц A и B
def matrix_AB(_A,_B):
     n = len(_A)
     _M = [[0]*(n+1) for _ in range(n)]
     for i in range(n):
          _M[i][n] = _B[i]
          for j in range(n):
               _M[i][j] = _A[i][j]
     return _M

#Показ матриц
def print_matrix(m, eps=1):
    for r in m:
        for elem in r:
            elem = f'{elem: .{eps}f}'
            print(f"{elem: ^6}", end=" ")
        print()
    print()

#Переворачивание матрицы 
def reverse(m):
    m_x = []
    for i in range(len(m)):
        m_x.append(m[len(m)-i-1])
    return m_x

#проверка A*X = B
def m_is_right(a,m_x):
    b = []
    for i in range(len(a)):
        sum_b = 0
        for j in range(len(a)):
            sum_b += a[i][j] * m_x[j]
        b.append(sum_b)
    return b
    
def remove_M(_m,_a,_b):
    _m[_a],_m[_b] = _m[_b], _m[_a]
    return _m

#Обратный ход гаусса
def gauss_downstep(M):
    n = len(M)
    M_X = []
    M_X.append(M[n - 1][n] / M[n - 1][n - 1])
    for i in range(n - 2, -1, -1):
        sum_x = 0
        for j in range(n - 1, i, -1):
            sum_x += M[i][j] * M_X[n - j - 1]
        X = (M[i][n] - sum_x) / M[i][i]
        M_X.append(X)
    M_X = reverse(M_X)
    # print('матрица X', M_X)
    # print()
    # print("Подстановка для проверки:")
    # print(m_is_right(A, M_X))
    # print()
    return M_X
#Метод гаусса
def gauss(_A,_B):
    M = matrix_AB(_A, _B)
    # print_matrix(M)
    n = len(M)

    for k in range(n-1):
        for i in range(k + 1, n):
            for j in range(k + 1, n + 1):
                M[i][j] = M[i][j] - (M[i][k] * M[k][j]) / M[k][k]
            M[i][k] = 0
    gauss_downstep(M)
    return M


#Метод гауса с выбором главного элемента (по столбцам)
def gauss_gl_el(_A,_B):
    M = matrix_AB(_A, _B)
    n = len(M)
    print_matrix(M)
    #Нахождение макс. элемента
    for k in range(n-1):
        max_el = M[k][k]
        num_el = k
        for j in range(k,n):
            if M[j][k] > max_el:
                max_el = M[j][k]
                num_el = j
        M = remove_M(M,k,num_el)
        #
    #Прямой ход
        for i in range(k + 1, n):
            for j in range(k + 1, n + 1):
                M[i][j] = M[i][j] - (M[i][k] * M[k][j]) / M[k][k]
            M[i][k] = 0
        print_matrix(M)
# Обратный ход
    gauss_downstep(M)
    # print_matrix(M)
    return M

def gauss_glav_el(M):
    n = len(M)
    # print_matrix(M)
    #Нахождение макс. элемента
    for k in range(n-1):
        max_el = M[k][k]
        num_el = k
        for j in range(k,n):
            if M[j][k] > max_el:
                max_el = M[j][k]
                num_el = j
        M = remove_M(M,k,num_el)
        if max_el == 0:
            print('trouble')
            print(k)
            M[k][k] = 1
    #Прямой ход
        for i in range(k + 1, n):
            for j in range(k + 1, n + 1):
                M[i][j] = M[i][j] - (M[i][k] * M[k][j]) / M[k][k]
            M[i][k] = 0
        # print_matrix(M)
# Обратный ход
    M_X = gauss_downstep(M)
    # print_matrix(M)
    return M, M_X

def gauss_LU(_A,_B):
    n = len(_A)
    M = gauss(_A, _B)
    U = [[0] * n for _ in range(n)]
    L = [[0] * n for _ in range(n)]

    for i in range(n):
        El = M[i][i]
        for j in range(n+1):
            M[i][j] = M[i][j] / El

    print_matrix(M)
    for i in range(n):
        for j in range(i,n):
            U[i][j] = M[i][j]
    print('U матрица')
    print_matrix(U)

    for i in range(0, n):
        L[i][0] = A[i][0]
        for j in range(1, n):
            sumKa = 0
            for k in range(j):
                sumKa += L[i][k] * U[k][j]
            L[i][j] = A[i][j] - sumKa
    print('L матрица')
    print_matrix(L)

    Y = [0] * n

    Y[0] = B[0]/L[0][0]

    for i in range(1,n):
        sumY = 0
        for j in range(0,i):
            sumY += L[i][j] * Y[j]
        Y[i] = (B[i] - sumY)/L[i][i]
    print('матрица Y')
    print(Y)
    print('')
    X = [0] * n
    for i in range(n-1,-1,-1):
        sumX = 0
        for j in range(i+1, n):
            sumX += U[i][j] * X[j]
        X[i] = Y[i] - sumX
    print('Матрица X')
    print(X)

    print('Подстановка для проверки:')
    print(m_is_right(A,X))



if __name__ == '__main__':
    print("Исходная матрица")
    print_matrix(matrix_AB(A,B))
    # gauss(A,B)
    gauss_gl_el(A,B)
    # gauss_LU(A,B)


