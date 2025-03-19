## Alunos: Michael Varaldo / Gustavo Chaves / Cristian Domingues


# Comparação de Algoritmos de Ordenação

## Requisitos

Antes de rodar o script, verifique se você tem os seguintes requisitos instalados:
- Python 3.x
- Virtualenv (opcional, mas recomendado)
- Dependências listadas no script

## Configurando o Ambiente Virtual

Para garantir que as dependências sejam instaladas corretamente sem interferir no sistema, utilize um ambiente virtual.

1. No terminal ou prompt de comando, navegue até a pasta do projeto:
   ```sh
   cd caminho/para/o/projeto
   ```
2. Crie um ambiente virtual:
   ```sh
   python -m venv venv
   ```
3. Ative o ambiente virtual:
   - No Windows:
     ```sh
     venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

## Instalando Dependências

O script utiliza bibliotecas externas que precisam ser instaladas. Para instalar todas as dependências necessárias, execute:
```sh
pip install opentelemetry-sdk
```

## Executando o Script

1. Certifique-se de que o ambiente virtual está ativado (ver passo anterior).
2. Execute o script Python:
   ```sh
   python main.py
   ```
3. O script solicitará a quantidade de números a serem gerados e ordenados. Digite um valor e pressione **Enter**.

## Saída e Logs

- O script gera um arquivo `unsorted_data.txt` contendo os dados gerados antes da ordenação.
- Após a execução, o script grava informações de desempenho no arquivo `sorting_logs.txt`, incluindo tempo de execução, número de comparações e trocas realizadas por cada algoritmo de ordenação.

## Estrutura do Projeto

```
projeto/
│── main.py  # Script principal
│── unsorted_data.txt  # Dados desordenados gerados
│── sorting_logs.txt  # Logs de execução
│── venv/  # Ambiente virtual (opcional)
```

## Observação
Caso queira adicionar mais algoritmos de ordenação, basta criar uma nova classe que herda de `SortingStrategy` e implementa o método `sort()`.

