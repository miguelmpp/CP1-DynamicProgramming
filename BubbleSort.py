# Algoritmo Bubble Sort em Python

# Leitura do tamanho do vetor
n = int(input("Quantos números você deseja digitar? "))

# Verifica se o tamanho inserido é válido 
if n <= 0:
    print("Tamanho inválido!")
else:
    # Inicializa o vetor e a contagem de trocas
    vet = []
    trocas = 0

    # Leitura dos elementos do vetor
    for i in range(n):
        numero = int(input(f"Digite o {i+1}º número: "))
        vet.append(numero)

    # Implementação do Bubble Sort
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

    # Exibe o vetor ordenado
    print("VETOR ORDENADO:", vet)

    # Exibe o número de trocas realizadas
    print("O número de trocas feitas neste vetor foi de", trocas)
