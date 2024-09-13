# DYNAMIC PROGRAMMING - Check Point 1

## 👥 Aluno
- **Miguel Mauricio Parrado Patarroyo** – RM554007

## 👨‍🏫 Professor
- Gabriel Sobral

## Descrição do Trabalho

Este trabalho envolve a implementação e análise de três algoritmos de ordenação: **Bubble Sort**, **Selection Sort**, e **Insertion Sort**. O objetivo é comparar a eficiência desses algoritmos com base no número de trocas realizadas em diferentes tipos de vetores.

## Explicação das Diferenças entre o Código 1 e o Código 2

### Código 1

O **Código 1** permite que o **usuário insira seus próprios vetores**. A estrutura geral segue a lógica:

1. O usuário informa o **tamanho do vetor** e insere os números.
2. O algoritmo de ordenação escolhido (Bubble Sort, Selection Sort ou Insertion Sort) é executado no vetor fornecido.
3. O vetor é ordenado e o **número de trocas realizadas** é exibido.

Essa abordagem é útil para testar o algoritmo com diferentes entradas e validar seu funcionamento de maneira interativa.

### Código 2

No **Código 2**, os vetores são **predefinidos** para diferentes casos de teste (crescente, decrescente e não ordenado), facilitando a **análise de desempenho**. Os principais pontos são:

1. **Três vetores predefinidos** são utilizados: um vetor ordenado em ordem crescente, outro em ordem decrescente e um vetor aleatório não ordenado.
2. O algoritmo de ordenação é aplicado a esses vetores.
3. O vetor ordenado e o **número de trocas realizadas** são mostrados ao final.

Este formato é mais adequado para uma **avaliação sistemática e comparativa** do desempenho dos algoritmos.

## Vetores Utilizados e Resultados

### Bubble Sort

- **Vetor ordenado em ordem crescente**: `[1, 2, 3, 4, 5, 6]`
  - Resultado após Bubble Sort: `[1, 2, 3, 4, 5, 6]`
  - Número de trocas: 0

- **Vetor ordenado em ordem decrescente**: `[6, 5, 4, 3, 2, 1]`
  - Resultado após Bubble Sort: `[1, 2, 3, 4, 5, 6]`
  - Número de trocas: 15

- **Vetor não ordenado**: `[5, 12, 2, 17, 23, 1]`
  - Resultado após Bubble Sort: `[1, 2, 5, 12, 17, 23]`
  - Número de trocas: 7

### Insertion Sort

- **Vetor ordenado em ordem crescente**: `[1, 2, 3, 4, 5]`
  - Resultado após Insertion Sort: `[1, 2, 3, 4, 5]`
  - Número de trocas: 0

- **Vetor ordenado em ordem decrescente**: `[5, 4, 3, 2, 1]`
  - Resultado após Insertion Sort: `[1, 2, 3, 4, 5]`
  - Número de trocas: 10

- **Vetor não ordenado**: `[5, 12, 2, 17, 23, 1]`
  - Resultado após Insertion Sort: `[1, 2, 5, 12, 17, 23]`
  - Número de trocas: 7

### Selection Sort

- **Vetor ordenado em ordem crescente**: `[1, 2, 3, 4, 5]`
  - Resultado após Selection Sort: `[1, 2, 3, 4, 5]`
  - Número de trocas: 0

- **Vetor ordenado em ordem decrescente**: `[5, 4, 3, 2, 1]`
  - Resultado após Selection Sort: `[1, 2, 3, 4, 5]`
  - Número de trocas: 2

- **Vetor não ordenado**: `[5, 12, 2, 17, 23, 1]`
  - Resultado após Selection Sort: `[1, 2, 5, 12, 17, 23]`
  - Número de trocas: 5

## Análise de Desempenho

Com base nos resultados apresentados para os três algoritmos de ordenação, a análise é a seguinte:

- **Vetor em ordem crescente**: Todos os algoritmos se comportam da mesma forma, sem realizar trocas.
- **Vetor em ordem decrescente**:
  - **Selection Sort**: 2 trocas
  - **Insertion Sort**: 10 trocas
  - **Bubble Sort**: 15 trocas
  O **Selection Sort** é mais eficiente nesse cenário.
- **Vetor não ordenado**:
  - **Selection Sort**: 5 trocas
  - **Insertion Sort**: 7 trocas
  - **Bubble Sort**: 7 trocas
  O **Selection Sort** também é o mais eficiente para vetores não ordenados.

## Conclusão

Com base no **número de trocas realizadas**, o **Selection Sort** é o algoritmo mais eficiente em geral, especialmente para vetores em ordem decrescente e não ordenados. O **Insertion Sort** é uma boa opção para vetores parcialmente ordenados, enquanto o **Bubble Sort** é o menos eficiente, exigindo mais trocas em vetores inversamente ordenados.

---

Caso tenha sugestões ou feedback, fique à vontade para entrar em contato.
