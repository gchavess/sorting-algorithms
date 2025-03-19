Explicação do Padrão Strategy Aplicado no Código

O código segue o padrão Strategy, permitindo a seleção dinâmica de algoritmos de ordenação sem modificar o código principal. Esse padrão é implementado por meio de uma interface abstrata SortingStrategy, que define um contrato para diferentes estratégias de ordenação. As classes concretas (BubbleSort, QuickSort, MergeSort, etc.) implementam esse contrato, possibilitando a substituição do algoritmo sem alterar a estrutura geral do código. Cada algoritmo pode ser executado de forma independente e comparado em relação a tempo de execução, número de comparações e trocas. No main, todas as estratégias são aplicadas ao mesmo conjunto de dados em sequência, utilizando a função execute_sorting(), que encapsula a lógica de execução e medição de desempenho. Isso permite flexibilidade e extensibilidade, pois novos algoritmos podem ser adicionados sem modificar o código existente. 

 

Descrição do Processo de Geração dos Dados

O processo de geração de dados foi projetado para criar conjuntos de números aleatórios de forma parametrizável, possibilitando a produção de volumes variados conforme a necessidade dos experimentos. Essa flexibilidade permite a avaliação do desempenho dos algoritmos de ordenação em diferentes cenários. A geração dos números ocorre por meio de uma função que produz valores aleatórios dentro de um intervalo predefinido, garantindo diversidade nos dados. Os números gerados são então armazenados em um arquivo, que pode estar no formato de texto (.txt) ou binário, dependendo dos requisitos do experimento. No formato de texto, os números são organizados em um arquivo .txt, onde cada valor é separado por quebras de linha ou um delimitador específico. Esse formato facilita a inspeção manual dos dados e sua utilização em diferentes ferramentas de análise. Essa abordagem assegura a criação rápida e eficiente dos conjuntos de dados, permitindo a execução de testes consistentes e a comparação do desempenho dos algoritmos de ordenação em bases de diferentes tamanhos. 

 

Análise dos Resultados

Qual algoritmo apresentou melhor desempenho em diferentes cenários?  
 
O QuickSort apresentou o melhor desempenho na maioria dos casos, seguido de perto pelo RadixSort, CountingSort e MergeSort. 
 

Por que apresentou melhor desempenho?                                     .  
 
O QuickSort é um algoritmo de ordenação eficiente com complexidade média O(n log n), o que explica sua rápida execução em comparação com algoritmos quadráticos como BubbleSort e InsertionSort.  
 
Além disso, não realiza trocas desnecessárias quando a partição é bem escolhida. O RadixSort e o CountingSort foram rápidos porque são algoritmos de ordenação linear O(n), mas funcionam bem apenas em números inteiros ou com restrições específicas. O MergeSort também apresentou um bom desempenho, pois tem complexidade garantida de O(n log n), mas é um pouco mais lento que o QuickSort devido ao overhead de alocação de memória adicional. 
 

Vale a pena usar a abordagem "Dividir e Conquistar" (ex: QuickSort, MergeSort)?  
 
Sim. Os algoritmos que usam essa abordagem (como QuickSort e MergeSort) foram muito mais rápidos do que os algoritmos quadráticos (BubbleSort, InsertionSort e SelectionSort). O QuickSort foi o mais eficiente no geral, enquanto o MergeSort apresentou um tempo um pouco maior devido à necessidade de mais memória. 

 
