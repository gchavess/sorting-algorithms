import matplotlib.pyplot as plt
from collections import defaultdict

def parse_log_file(filename):
    data = defaultdict(lambda: {'execution_time': [], 'comparisons': [], 'swaps': [], 'dataset_sizes': []})
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(' | ')
            if len(parts) != 5:
                continue
            algo = parts[0].split(' - ')[1].strip()
            dataset_size = int(parts[1].split(': ')[1])
            exec_time = float(parts[2].split(': ')[1].split()[0])
            comparisons = int(parts[3].split(': ')[1])
            swaps = int(parts[4].split(': ')[1])
            
            data[algo]['execution_time'].append(exec_time)
            data[algo]['comparisons'].append(comparisons)
            data[algo]['swaps'].append(swaps)
            data[algo]['dataset_sizes'].append(dataset_size)
    return data

filename = 'sorting_logs.txt'
data = parse_log_file(filename)

algorithms = list(data.keys())

execution_time_1000 = [data[algo]['execution_time'][data[algo]['dataset_sizes'].index(1000)] for algo in algorithms]
execution_time_5000 = [data[algo]['execution_time'][data[algo]['dataset_sizes'].index(5000)] for algo in algorithms]
execution_time_10000 = [data[algo]['execution_time'][data[algo]['dataset_sizes'].index(10000)] for algo in algorithms]
comparisons_5000 = [data[algo]['comparisons'][data[algo]['dataset_sizes'].index(5000)] for algo in algorithms]

plt.figure(figsize=(12, 6))
plt.bar(algorithms, execution_time_10000, color='skyblue')
plt.yscale('log')
plt.title('Tempo de Execução por Algoritmo (Dataset 10000)')
plt.xlabel('Algoritmo')
plt.ylabel('Tempo (segundos, escala log)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

selected_algos = ['BubbleSort', 'QuickSort', 'MergeSort', 'RadixSort']
plt.figure(figsize=(12, 6))
for algo in selected_algos:
    times = [data[algo]['execution_time'][data[algo]['dataset_sizes'].index(size)] for size in [1000, 5000, 10000]]
    plt.plot([1000, 5000, 10000], times, label=algo, marker='o')
plt.yscale('log')
plt.title('Escalabilidade do Tempo de Execução')
plt.xlabel('Tamanho do Dataset')
plt.ylabel('Tempo (segundos, escala log)')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
plt.scatter(comparisons_5000, execution_time_5000, color='purple')
for i, algo in enumerate(algorithms):
    plt.annotate(algo, (comparisons_5000[i], execution_time_5000[i]), fontsize=8, xytext=(5, 5), textcoords='offset points')
plt.xscale('log')
plt.yscale('log')
plt.title('Comparações vs. Tempo de Execução (Dataset 5000)')
plt.xlabel('Número de Comparações (escala log)')
plt.ylabel('Tempo (segundos, escala log)')
plt.grid(True, which="both", ls="--")
plt.tight_layout()
plt.show()