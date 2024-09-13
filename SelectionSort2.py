def selection_sort(vet):
    """
    Função que ordena um vetor usando o método Selection Sort.
    Retorna o vetor ordenado e o número de trocas realizadas.
    """
    n = len(vet)
    trocas = 0
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if vet[j] < vet[min_index]:
                min_index = j
        if min_index != i:
            vet[i], vet[min_index] = vet[min_index], vet[i]
            trocas += 1
    return vet, trocas

# Vetor ordenado em ordem crescente
vetor_crescente = [1, 2, 3, 4, 5]
print("Vetor ordenado em ordem crescente:", vetor_crescente)
vetor_ordenado_crescente, trocas_crescente = selection_sort(vetor_crescente.copy())
print("Resultado após Selection Sort:", vetor_ordenado_crescente)
print("Número de trocas:", trocas_crescente)

# Vetor ordenado em ordem decrescente
vetor_decrescente = [5, 4, 3, 2, 1]
print("\nVetor ordenado em ordem decrescente:", vetor_decrescente)
vetor_ordenado_decrescente, trocas_decrescente = selection_sort(vetor_decrescente.copy())
print("Resultado após Selection Sort:", vetor_ordenado_decrescente)
print("Número de trocas:", trocas_decrescente)

# Vetor não ordenado
vetor_nao_ordenado = [5, 12, 2, 17, 23, 1]
print("\nVetor não ordenado:", vetor_nao_ordenado)
vetor_ordenado_nao_ordenado, trocas_nao_ordenado = selection_sort(vetor_nao_ordenado.copy())
print("Resultado após Selection Sort:", vetor_ordenado_nao_ordenado)
print("Número de trocas:", trocas_nao_ordenado)
