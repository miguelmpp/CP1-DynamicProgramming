def bubble_sort(vet):
    """
    Função que ordena um vetor usando o método Bubble Sort.
    Retorna o vetor ordenado e o número de trocas realizadas.
    """
    n = len(vet)
    trocas = 0
    u = n
    while u > 1:
        iu = 0
        for j in range(1, u):
            if vet[j-1] > vet[j]:
                # Troca os elementos
                vet[j], vet[j-1] = vet[j-1], vet[j]
                iu = j
                trocas += 1
        u = iu
    return vet, trocas

# Vetor ordenado em ordem crescente
vetor_crescente = [1, 2, 3, 4, 5, 6]
print("Vetor ordenado em ordem crescente:", vetor_crescente)
vetor_ordenado_crescente, trocas_crescente = bubble_sort(vetor_crescente.copy())
print("Resultado após Bubble Sort:", vetor_ordenado_crescente)
print("Número de trocas:", trocas_crescente)

# Vetor ordenado em ordem decrescente
vetor_decrescente = [6, 5, 4, 3, 2, 1]
print("\nVetor ordenado em ordem decrescente:", vetor_decrescente)
vetor_ordenado_decrescente, trocas_decrescente = bubble_sort(vetor_decrescente.copy())
print("Resultado após Bubble Sort:", vetor_ordenado_decrescente)
print("Número de trocas:", trocas_decrescente)

# Vetor não ordenado
vetor_nao_ordenado = [5, 12, 2, 17, 23, 1]
print("\nVetor não ordenado:", vetor_nao_ordenado)
vetor_ordenado_nao_ordenado, trocas_nao_ordenado = bubble_sort(vetor_nao_ordenado.copy())
print("Resultado após Bubble Sort:", vetor_ordenado_nao_ordenado)
print("Número de trocas:", trocas_nao_ordenado)
