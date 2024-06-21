M = [[5,4,0,0,0,0,0,0,0,0,0],
     [-5,0,-3,4,5,0,0,0,0,0,0],
     [0,-4,3,0,0,1,2,0,0,0,0],
     [0,0,0,-4,0,-1,0,-14,12,0,0],
     [0,0,0,0,-5,0,0,14,0,6,0],
     [0,0,0,0,0,0,-2,0,-12,0,10],
     [0,0,0,0,0,0,0,0,0,-6,-10]]
print("До сортировки:")
print('\n'.join('\t'.join(map(str, row)) for row in M))
print()
def topol_sort(M):
    for h in range(len(M)):
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] < 0:
                    work_with_column(M, i, j)
def work_with_column(M, stroka,j):
    for i in range(stroka, len(M)):
        if M[i][j] > 0:
            swap_stroki(stroka, i)
            break
def swap_stroki(index1, index2):
    M[index2], M[index1] = M[index1], M[index2]
topol_sort(M)
def dinam_prog(M):
    dictionary = dict()
    for i in range(len(M)):
        dictionary[f"l{i}"] = 0
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] > 0:
                help_per = find_ways(M, i, j)
                l = "l" + str(help_per[0])
                weight = help_per[1]
                if dictionary["l" + str(i)] + weight < dictionary[l]:
                    dictionary[l] = dictionary["l" + str(i)] + weight
                else:
                    if dictionary[l] == 0:
                        dictionary[l] = dictionary["l" + str(i)] + weight
    print(dictionary)
    print()
def find_ways(M, i, j):
    weight = 0
    way = 0
    for index1 in range(i, len(M)):
        if M[index1][j] < 0:
            way = index1
            weight = M[index1][j]
    return way, abs(weight)

print("После сортировки:")
print('\n'.join('\t'.join(map(str, row)) for row in M))
print("Длины путей:")
dinam_prog(M)