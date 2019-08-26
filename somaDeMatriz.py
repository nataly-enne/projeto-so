def somarMatrizes(matriz1, matriz2):
    if(len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0])):
        return None
    result = []
    for i in range(len(matriz1)):   
        result.append([])
        for j in range(len(matriz1[0])):
            result[i].append(matriz1[i][j] + matriz2[i][j])
    return result

def somarElemento(i, j):
	matriz3[i][j].append(matriz1[i][j] + matriz2[i][j])


matriz1 =	[[1, 2, 3, 4],
		[2, 3, 4, 5],
		[2, 4, 5, 6],
		[5, 6, 7, 8]]

matriz2 = 	[[1, 3, 5, 6],
		[3, 4, 5, 6],
		[5, 6, 7, 2],
		[1, 2, 4, 5]]

matriz3 =       [[0,0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]


for i in range (len(matriz1)):
	for j in range (len(matriz2[0])):
		somarElemento(i, j)
print(matriz3)
soma = somarMatrizes(matriz1, matriz2)
if soma is not None:
	for i in soma:
		print(i)
	else:
		print('Matrizes devem conter o mesmo numero de linhas e colunas')
