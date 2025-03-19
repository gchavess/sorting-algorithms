# Explicação do Padrão Strategy Aplicado no Código

O código segue o padrão Strategy, permitindo a seleção dinâmica de algoritmos de ordenação sem modificar o código principal. Esse padrão é implementado por meio de uma interface abstrata SortingStrategy, que define um contrato para diferentes estratégias de ordenação. As classes concretas (BubbleSort, QuickSort, MergeSort, etc.) implementam esse contrato, possibilitando a substituição do algoritmo sem alterar a estrutura geral do código. Cada algoritmo pode ser executado de forma independente e comparado em relação a tempo de execução, número de comparações e trocas. No main, todas as estratégias são aplicadas ao mesmo conjunto de dados em sequência, utilizando a função execute_sorting(), que encapsula a lógica de execução e medição de desempenho. Isso permite flexibilidade e extensibilidade, pois novos algoritmos podem ser adicionados sem modificar o código existente. 

 

# Descrição do Processo de Geração dos Dados

O processo de geração de dados foi projetado para criar conjuntos de números aleatórios de forma parametrizável, possibilitando a produção de volumes variados conforme a necessidade dos experimentos. Essa flexibilidade permite a avaliação do desempenho dos algoritmos de ordenação em diferentes cenários. A geração dos números ocorre por meio de uma função que produz valores aleatórios dentro de um intervalo predefinido, garantindo diversidade nos dados. Os números gerados são então armazenados em um arquivo, que pode estar no formato de texto (.txt) ou binário, dependendo dos requisitos do experimento. No formato de texto, os números são organizados em um arquivo .txt, onde cada valor é separado por quebras de linha ou um delimitador específico. Esse formato facilita a inspeção manual dos dados e sua utilização em diferentes ferramentas de análise. Essa abordagem assegura a criação rápida e eficiente dos conjuntos de dados, permitindo a execução de testes consistentes e a comparação do desempenho dos algoritmos de ordenação em bases de diferentes tamanhos. 

# Ferramenta Utilizada e Análise dos Resultados
Para a visualização e análise dos logs gerados durante a execução dos algoritmos de ordenação, foi utilizada a ferramenta open-source Jaeger. Essa ferramenta é amplamente empregada para rastreamento distribuído, permitindo monitorar o desempenho das operações e identificar gargalos no processamento. Com a utilização do Jaeger, foi possível coletar dados detalhados sobre o tempo de execução, número de comparações e trocas realizadas por cada algoritmo, facilitando a análise de eficiência.

Os resultados obtidos confirmam a superioridade dos algoritmos baseados em Dividir e Conquistar, como QuickSort e MergeSort, que apresentaram tempos de execução significativamente menores em comparação aos métodos quadráticos, como BubbleSort e InsertionSort. O QuickSort foi consistentemente o mais eficiente, com tempo de execução variando de 0,002 segundos para um conjunto de 1000 elementos até 0,026 segundos para 10000 elementos. O RadixSort e o CountingSort, por serem algoritmos de complexidade O(n), também demonstraram alto desempenho, mas são aplicáveis apenas a números inteiros.

Por outro lado, algoritmos quadráticos como BubbleSort e SelectionSort demonstraram tempos de execução excessivamente altos, tornando-os inviáveis para grandes conjuntos de dados. Com 10000 elementos, o BubbleSort levou mais de 12 segundos, enquanto o QuickSort finalizou em menos de 0,03 segundos, evidenciando a importância da escolha do algoritmo adequado conforme o tamanho do dataset.

O uso do Jaeger foi essencial para a captura e visualização desses tempos de execução e contagens de operações, permitindo uma avaliação objetiva do desempenho dos algoritmos testados. 

# Análise dos Resultados

## Qual algoritmo apresentou melhor desempenho em diferentes cenários?  
 
O QuickSort apresentou o melhor desempenho na maioria dos casos, seguido de perto pelo RadixSort, CountingSort e MergeSort. 
 

## Por que apresentou melhor desempenho?                                     .  
 
O QuickSort é um algoritmo de ordenação eficiente com complexidade média O(n log n), o que explica sua rápida execução em comparação com algoritmos quadráticos como BubbleSort e InsertionSort.  
Além disso, não realiza trocas desnecessárias quando a partição é bem escolhida. O RadixSort e o CountingSort foram rápidos porque são algoritmos de ordenação linear O(n), mas funcionam bem apenas em números inteiros ou com restrições específicas. O MergeSort também apresentou um bom desempenho, pois tem complexidade garantida de O(n log n), mas é um pouco mais lento que o QuickSort devido ao overhead de alocação de memória adicional. 
 

## Vale a pena usar a abordagem "Dividir e Conquistar" (ex: QuickSort, MergeSort)?  
 
Sim. Os algoritmos que usam essa abordagem (como QuickSort e MergeSort) foram muito mais rápidos do que os algoritmos quadráticos (BubbleSort, InsertionSort e SelectionSort). O QuickSort foi o mais eficiente no geral, enquanto o MergeSort apresentou um tempo um pouco maior devido à necessidade de mais memória. 

 
