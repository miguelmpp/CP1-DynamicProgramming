def selection_sort(vet):
    """
    Função que ordena um vetor usando o método Selection Sort.
    Retorna o vetor ordenado e o número de trocas realizadas.
    """
    n = len(vet)
    trocas = 0
    
    # Implementação do Selection Sort
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if vet[j] < vet[min_idx]:
                min_idx = j
        
        # Verifica se houve troca
        if min_idx != i:
            vet[i], vet[min_idx] = vet[min_idx], vet[i]
            trocas += 1
    
    return vet, trocas

# Leitura do tamanho do vetor
n = int(input("Quantos números você deseja digitar? "))

# Verifica se o tamanho inserido é válido (removendo a limitação de 10)
if n <= 0:
    print("Tamanho inválido!")
else:
    # Leitura dos elementos do vetor
    vet = []
    for i in range(n):
        numero = int(input(f"Digite o {i+1}º número: "))
        vet.append(numero)

    # Ordenação do vetor
    vet_ordenado, num_trocas = selection_sort(vet)

    # Exibe o vetor ordenado e o número de trocas
    print("\nVETOR ORDENADO:", vet_ordenado)
    print(f"Número de trocas: {num_trocas}")
