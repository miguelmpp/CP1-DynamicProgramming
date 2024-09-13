def insertion_sort(vet):
    """
    Função que ordena um vetor usando o método Insertion Sort.
    Retorna o vetor ordenado e o número de trocas realizadas.
    """
    n = len(vet)
    trocas = 0

    for i in range(1, n):
        key = vet[i]
        j = i - 1
        while j >= 0 and vet[j] > key:
            vet[j + 1] = vet[j]
            j -= 1
            trocas += 1
        vet[j + 1] = key

    return vet, trocas

# Leitura do tamanho do vetor
n = int(input("Quantos números você deseja digitar? "))

# Leitura dos elementos do vetor
vet = []
for i in range(n):
    numero = int(input(f"Digite o {i+1}º número: "))
    vet.append(numero)

# Ordenação do vetor
vet_ordenado, num_trocas = insertion_sort(vet)

# Exibe o vetor ordenado e o número de trocas
print("\nVETOR ORDENADO:", vet_ordenado)
print(f"Número de trocas: {num_trocas}")
