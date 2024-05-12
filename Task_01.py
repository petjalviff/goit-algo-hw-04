import random
import timeit

# Код сорутвання методом злиття:
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k +=1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Функція сортування методом вставки
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key  < arr[j]:
            arr[j +1] = arr[j]
            j -= 1
        arr[j +1] = key

# Функція створення рамдомних масивів
def generate_random_array(size):
    # print([random.randint(1, 1000) for _ in range(size)])
    return [random.randint(1, 5000) for _ in range(size)]

# Тестові набори даних різного розміру
sizes = [50, 500, 5000]

# Визначення часу виконання кожного алгоритму сортування для відповідного розміру
times = {"merge_sort": [], "insertion_sort": [], "timsort": []}

for size in sizes:
    random_array = generate_random_array(size)
    print(f"random_array for size {size} is: ", random_array)
    print()

    # Таймінг сортування методом злиття
    times["merge_sort"].append(
        timeit.timeit("merge_sort(random_array.copy())", globals=globals(), number=1)
    )

    # Таймінг сортування методом вставки
    times["insertion_sort"].append(
        timeit.timeit("insertion_sort(random_array.copy())", globals=globals(), number=1)
    )

    # Таймінг сортвання методом Timsort
    times["timsort"].append(
        timeit.timeit("sorted(random_array)", globals=globals(), number=1)
    )

# Форматування таблиці з результатами
header = f"| {'Size':<15} | {'Merge Sort':<15} | {'Insertion Sort':<15} | {'Timsort':<15} |"

separator = "-" * len(header)

data_rows = "\n".join(
    [f"| {size:<15} | {times['merge_sort'][i]:<15.6f} | {times['insertion_sort'][i]:<15.6f} | {times['timsort'][i]:<15.6f} |" 
     for i, size in enumerate(sizes)]
)

table = f"{header}\n{separator}\n{data_rows}"

print(table)