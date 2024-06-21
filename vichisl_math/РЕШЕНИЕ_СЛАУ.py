# A = [
#     [4, 3, 2, 1, 3],
#     [3, 6, 4, 2, 6],
#     [2, 4, 6, 3, 4],
#     [1, 2, 3, 4, 7]
# ]
# def method_gaussa(A):
#     n = len(A[0])
#     for i in range(1, len(A)):
#         delitel = A[i - 1][i - 1]
#         for k in range(i - 1, n):
#             A[i - 1][k] = A[i - 1][k] / delitel
#         for j in range(i, n - 1):
#             A[j][j - 1] = A[j][j - 1] - (A[i - 1][j - 1] * A[j][j - 1])
# method_gaussa(A)
# print(*A, sep='\n')
# def method_gaussa(A):
#     a = 0
#     n = len(A[0])
#     delitel = A[a][a]
#     for i in range(0, n):
#         A[a][i] = A[a][i] / delitel
#     for i in range(1, len(A)):
#         for j in range(0, n):
#             A[i][j] = A[i][j] - (A[a][j] * A[i][j])
#     a += 1
#     return a
# print(method_gaussa(A))
# print(*A, sep='\n')

with open("gausse.txt", 'r') as file:
    lines = file.readlines()
A = []
for line in lines:
    numbers = line.split(' ')
    numbers = [float(number) for number in numbers]
    A.append(numbers)
print('Исходная матрица:')
print(*A, sep='\n')
print('Ответ:')
def method_gaussa(A):
    # Прямой ход
    for i in range(len(A)):
        for k in range(i + 1, len(A)):
            result = A[k][i] / A[i][i]
            for j in range(len(A) + 1):
                A[k][j] -= result * A[i][j]
    #Обратный ход
    otvet = [0] * len(A)
    otvet[-1] = A[-1][-1] / A[-1][len(A) - 1]
    for i in range(len(A) - 1, -1, -1):
        otvet[i] = (A[i][-1] - sum([A[i][j] * otvet[j] for j in range(i + 1, len(A))])) / A[i][i]
    return otvet
print("Метод Гаусса")
print(*method_gaussa(A), sep='\n')
print('---------------------------')
print('Конечная матрица:')
print(*A, sep='\n')



with open("gausse.txt", 'r') as file:
    lines = file.readlines()
A = []
for line in lines:
    numbers = line.split(' ')
    numbers = [float(number) for number in numbers]
    A.append(numbers)
print('Исходная матрица:')
print(*A, sep='\n')
print('Ответ:')

def method_gaussa_vibor(A):
    # Прямой ход
    for i in range(len(A)):
        swap_srtoki(A, i)
        # print('---------------------------------------')
        # print(*A, sep='\n')
        for k in range(i + 1, len(A)):
            result = A[k][i] / A[i][i]
            for j in range(len(A) + 1):
                A[k][j] -= result * A[i][j]
    # Обратный ход
    otvet = [0] * len(A)
    otvet[-1] = A[-1][-1] / A[-1][len(A) - 1]
    for i in range(len(A) - 1, -1, -1):
        try:
            otvet[i] = (A[i][-1] - sum([A[i][j] * otvet[j] for j in range(i + 1, len(A)) if A[i][j] != 0])) / A[i][i]
        except ZeroDivisionError:
            otvet[i] = 0
    return otvet
def find_max(A, stolbec):
    max_el = -10**10
    num_stroki = 0
    for j in range(len(A)):
        if max_el < A[j][stolbec]:
            max_el, num_stroki = A[j][stolbec], j
    return num_stroki
def swap_srtoki(A, i):
    result = find_max(A, i)
    A[i], A[result] = A[result], A[i]
print("Метод Гаусса с выбором")
print(*method_gaussa_vibor(A), sep='\n')


# print('-----------')
# print('Конечная матрица:')
# print(*A, sep='\n')

#
# #LU РАЗЛОЖЕНИЕ
# with open("gausse.txt", 'r') as file:
#     lines = file.readlines()
# A = []
# for line in lines:
#     numbers = line.split(' ')
#     numbers = [float(number) for number in numbers]
#     A.append(numbers)
# print('Исходная матрица:')
# print(*A, sep='\n')
# print('Ответ:')
#
# with open("gausse.txt", 'r') as file:
#     lines = file.readlines()
# U = []
# for line in lines:
#     numbers = line.split(' ')
#     numbers = [float(number) for number in numbers]
#     A.append(numbers)
# print('Исходная матрица:')
# print(*A, sep='\n')
# print('Ответ:')
#
# with open("gausse.txt", 'r') as file:
#     lines = file.readlines()
# L = []
# for line in lines:
#     numbers = line.split(' ')
#     numbers = [float(number) for number in numbers]
#     A.append(numbers)
# print('Исходная матрица:')
# print(*A, sep='\n')
# print('Ответ:')
#
# def LU(A, L, U):
#     # Получение U матрицы
#     for i in range(len(U)):
#         for k in range(i + 1, len(A)):
#             result = U[k][i] / A[i][i]
#             for j in range(len(A) + 1):
#                 U[k][j] -= result * U[i][j]
#     # Получение L матрицы
#     for i in range(len(L)):
#         for j in range(i + 1, len(A)):
#             L[i][j] = A[i][j] - sum(L[i][j - 1]) * U[i][j]
# LU(A, L, U)
# print(*L, sep='\n')
# print('----------------------------------------------------')
# print(*U, sep='\n')
