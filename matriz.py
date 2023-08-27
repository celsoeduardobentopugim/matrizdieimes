import numpy as np

dieimes_matriz = np.array([[3, 4, 1], [3, 2, 1]])

total_soma = 0
for linha in dieimes_matriz:
    for elemento in linha:
        total_soma += elemento

print(f"A soma de todos os elementos da matriz é:{total_soma}")