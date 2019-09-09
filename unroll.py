# -- coding: utf-8 --
import threading
import numpy as np
import os
import random
import time

time.time

# def somarMatrizes(matriz1, matriz2):
#     if(len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0])):
#         return None
#     result = []
#     for i in range(len(matriz1)):   
#         result.append([])
#         for j in range(len(matriz1[0])):
#             result[i].append(matriz1[i][j] + matriz2[i][j])
#     return result

# def somarElemento(i, j):
# 	matriz3[i][j].append(matriz1[i][j] + matriz2[i][j])

def func (matriz1, matriz2, i, j, method, op, result):
    if method == 'thread':
        threading.currentThread()
        if op == 'soma':
            result[0][0][i][j] = matriz1 + matriz2

        if op == 'mult':
            for item in range(len(matriz1)):
                result[1][0][i][j] += matriz1[item] * matriz2[item]


def unroll(args, method, op, results):
    if method == "thread":
        for arg in args:
            t = threading.Thread(target = func, args = (arg[0], arg[1], arg[2], arg[3], method, op, results))
            t.start()
        

def get_columns(matriz, c):
    coluna = [0 for i in range(len(matriz))]
    
    for i in range(len(matriz[0])):
        coluna[i] = matriz[i][c]
    
    return coluna

## gerando args de soma
def get_sum_args():
    args = [[0 for i in range(4)] for i in range(SIZE * SIZE)]
    row_args = 0
    
    for r in range(SIZE):
        for c in range(SIZE):
            args[row_args] = [matriz_randomica1[r][c], matriz_randomica2[r][c], r, c]
            row_args += 1
    return args

## gerando args de multiplicação
def get_prod_args():
    args = [[0 for i in range(4)] for i in range(SIZE * SIZE)]
    row_args = 0

    for r in range(SIZE):
        for c in range(SIZE):
            args[row_args] = [matriz_randomica1[r], get_columns(matriz_randomica2, c), r, c]
            row_args += 1
    return args

## impressão da matriz
def print_matriz(matriz, size, text):
    print(text)
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matriz]))
    print('\n')

############################################ MAIN ############################################

SIZE = 3 # tamanho generico



matriz_randomica1 = np.random.randint(10, size = (SIZE, SIZE)) # gerar matriz
matriz_randomica2 = np.random.randint(10, size = (SIZE, SIZE)) # gerar matriz

result_thread_soma = np.full((SIZE, SIZE), 0) # preencher tudo com zero pra popualr a matriz pra criar na memoria e n dar erro
result_thread_mult = np.full((SIZE, SIZE), 0)

results = [[result_thread_soma], [result_thread_mult]] # matriz das matrizes

time_before = time.time()

args = get_sum_args()
unroll(args, 'thread', 'soma', results)


args = get_prod_args()
unroll(args,'thread', 'mult', results)

time_after = time.time()

time_after -= time_before

print_matriz(matriz_randomica1, SIZE, "Matriz 1:")
print_matriz(matriz_randomica2, SIZE, "Matriz 2:")
print_matriz(results[0][0], SIZE * SIZE, "Resultado da soma [THREADS]:")
print_matriz(results[1][0], SIZE * SIZE, "Resultado da multiplicação [THREADS]:")

print(time_after)