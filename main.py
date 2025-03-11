import time
import random
import logging
from abc import ABC, abstractmethod
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

tracer_provider = TracerProvider()
tracer_provider.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))
trace.set_tracer_provider(tracer_provider)
tracer = trace.get_tracer(__name__)

logging.basicConfig(filename='sorting_logs.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def save_to_file(filename, data):
    with open(filename, "w") as file:
        file.write("\n".join(map(str, data)))
        
class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

class TimSort(SortingStrategy):
    def sort(self, data):
        self.comparisons = 0
        self.swaps = 0
        self.tim_sort(data)
        return data, self.comparisons, self.swaps

    def insertion_sort(self, data, left, right):
        for i in range(left + 1, right + 1):
            key = data[i]
            j = i - 1
            while j >= left and data[j] > key:
                self.comparisons += 1  
                data[j + 1] = data[j]
                j -= 1
                self.swaps += 1 
            data[j + 1] = key

    def merge(self, data, l, m, r):
        left = data[l:m + 1]
        right = data[m + 1:r + 1]

        i = j = 0
        k = l

        while i < len(left) and j < len(right):
            self.comparisons += 1  
            if left[i] <= right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
                self.swaps += 1  
            k += 1

        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1

    def tim_sort(self, data):
        n = len(data)
        RUN = 32

        for i in range(0, n, RUN):
            self.insertion_sort(data, i, min(i + RUN - 1, n - 1))

        size = RUN
        while size < n:
            for left in range(0, n, 2 * size):
                mid = min(n - 1, left + size - 1)
                right = min(n - 1, left + 2 * size - 1)
                if mid < right:
                    self.merge(data, left, mid, right)
            size *= 2

class BubbleSort(SortingStrategy):
    def sort(self, data):
        comparisons, swaps = 0, 0
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                comparisons += 1
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    swaps += 1
        return data, comparisons, swaps

class BubbleSortOptimized(SortingStrategy):
    def sort(self, data):
        comparisons, swaps = 0, 0
        n = len(data)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                comparisons += 1
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    swaps += 1
                    swapped = True
            if not swapped:
                break
        return data, comparisons, swaps

class InsertionSort(SortingStrategy):
    def sort(self, data):
        comparisons, swaps = 0, 0
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and key < data[j]:
                comparisons += 1
                data[j + 1] = data[j]
                j -= 1
                swaps += 1
            data[j + 1] = key
        return data, comparisons, swaps

class SelectionSort(SortingStrategy):
    def sort(self, data):
        comparisons, swaps = 0, 0
        n = len(data)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                comparisons += 1
                if data[j] < data[min_idx]:
                    min_idx = j
            data[i], data[min_idx] = data[min_idx], data[i]
            swaps += 1
        return data, comparisons, swaps

class QuickSort(SortingStrategy):
    def sort(self, data):
        comparisons, swaps = 0, 0
        
        def quicksort_helper(arr):
            nonlocal comparisons, swaps
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            comparisons += len(arr) - 1
            return quicksort_helper(left) + middle + quicksort_helper(right)

        sorted_data = quicksort_helper(data)
        return sorted_data, comparisons, swaps

class RadixSort(SortingStrategy):
    def sort(self, data):
        if not data:
            return []
        
        max_val = max(data)
        exp = 1
        while max_val // exp > 0:
            self.counting_sort(data, exp)
            exp *= 10
        return data
    
    def counting_sort(self, data, exp):
        n = len(data)
        output = [0] * n
        count = [0] * 10
        
        for i in range(n):
            index = (data[i] // exp) % 10
            count[index] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]
        
        for i in range(n - 1, -1, -1):
            index = (data[i] // exp) % 10
            output[count[index] - 1] = data[i]
            count[index] -= 1

        for i in range(n):
            data[i] = output[i]

class ShellSort(SortingStrategy):
    def sort(self, data):
        n = len(data)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = data[i]
                j = i
                while j >= gap and data[j - gap] > temp:
                    data[j] = data[j - gap]
                    j -= gap
                data[j] = temp
            gap //= 2
        return data

class MergeSort(SortingStrategy):
    def sort(self, data):
        comparisons, swaps = 0, 0
        
        def merge_sort_helper(arr):
            nonlocal comparisons, swaps
            if len(arr) > 1:
                mid = len(arr) // 2
                left_half = merge_sort_helper(arr[:mid])
                right_half = merge_sort_helper(arr[mid:])
                merged = []
                i = j = 0
                while i < len(left_half) and j < len(right_half):
                    comparisons += 1
                    if left_half[i] < right_half[j]:
                        merged.append(left_half[i])
                        i += 1
                    else:
                        merged.append(right_half[j])
                        j += 1
                        swaps += 1
                merged.extend(left_half[i:])
                merged.extend(right_half[j:])
                return merged
            return arr

        sorted_data = merge_sort_helper(data)
        return sorted_data, comparisons, swaps

class HeapSort(SortingStrategy):
    def sort(self, data):
        comparisons, swaps = 0, 0
        def heapify(arr, n, i):
            nonlocal comparisons, swaps
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < n and arr[i] < arr[l]:
                comparisons += 1
                largest = l
            if r < n and arr[largest] < arr[r]:
                comparisons += 1
                largest = r
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                swaps += 1
                heapify(arr, n, largest)
        n = len(data)
        for i in range(n // 2 - 1, -1, -1):
            heapify(data, n, i)
        for i in range(n - 1, 0, -1):
            data[i], data[0] = data[0], data[i]
            swaps += 1
            heapify(data, i, 0)
        return data, comparisons, swaps


class CountingSort(SortingStrategy):
    def sort(self, data):
        if not data:
            return [], 0, 0
        max_val = max(data)
        min_val = min(data)
        range_of_elements = max_val - min_val + 1
        count_array = [0] * range_of_elements
        output_array = [0] * len(data)

        for num in data:
            count_array[num - min_val] += 1

        for i in range(1, len(count_array)):
            count_array[i] += count_array[i - 1]

        for num in reversed(data):
            output_array[count_array[num - min_val] - 1] = num
            count_array[num - min_val] -= 1

        return output_array, 0, 0

class RadixSort(SortingStrategy):
    def sort(self, data):
        if not data:
            return [], 0, 0
        max_val = max(data)
        exp = 1
        while max_val // exp > 0:
            self.counting_sort(data, exp)
            exp *= 10
        return data, 0, 0

    def counting_sort(self, data, exp):
        n = len(data)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = (data[i] // exp) % 10
            count[index] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            index = (data[i] // exp) % 10
            output[count[index] - 1] = data[i]
            count[index] -= 1

        for i in range(n):
            data[i] = output[i]

class ShellSort(SortingStrategy):
    def sort(self, data):
        n = len(data)
        comparisons, swaps = 0, 0
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = data[i]
                j = i
                while j >= gap and data[j - gap] > temp:
                    comparisons += 1
                    data[j] = data[j - gap]
                    j -= gap
                    swaps += 1
                data[j] = temp
            gap //= 2
        return data, comparisons, swaps

def execute_sorting(algorithm, data):
    with tracer.start_as_current_span(algorithm.__class__.__name__) as span:
        start_time = time.time()
        sorted_data, comparisons, swaps = algorithm.sort(data.copy())
        execution_time = time.time() - start_time
        log_message = (f'{algorithm.__class__.__name__} | Dataset Size: {len(data)} | '
                       f'Execution Time: {execution_time:.6f} seconds | '
                       f'Comparisons: {comparisons} | Swaps: {swaps}')
        logging.info(log_message)
        span.set_attribute("algorithm", algorithm.__class__.__name__)
        span.set_attribute("dataset_size", len(data))
        span.set_attribute("execution_time", execution_time)
        return sorted_data

if __name__ == "__main__":
    size = int(input("Digite a quantidade de dados a serem gerados: "))
    data = [random.randint(0, 100000) for _ in range(size)]
    save_to_file("unsorted_data.txt", data)

    algorithms = [BubbleSort(), BubbleSortOptimized(), InsertionSort(), SelectionSort(), QuickSort(), MergeSort(), HeapSort(), TimSort(), CountingSort(), RadixSort(), ShellSort()]
    
    for algo in algorithms:
        execute_sorting(algo, data)