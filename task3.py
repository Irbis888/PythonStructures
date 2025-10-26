# здесь я реализую пару алгоритмов сортировки: merge sort
# и Timsort. Потом сравним скорости

import math
import random
import timeit


def timsort(arr):
    # это - сортировка Timsort
    # подобный алгоритм применяется в функции sorted(arr)
    n = len(arr)
    MIN_RUN = 128 # можно и другое значение,
    # но тут вижу баланс между почти отсортированными и случайными массивами

    # Сортируем маленькие подмассивы insertionом
    for i in range(0, n, MIN_RUN):
        end = min(i + MIN_RUN, n)
        insertion_sort(arr, i, end)

    # Сливаем участки побольше
    size = MIN_RUN
    while size < n:
        for start in range(0, n, 2 * size):
            mid = min(start + size, n)
            end = min(start + 2 * size, n)

            if mid < end:
                # мерджим участки массива arr
                merge(arr, start, mid, end)

        size *= 2

    return arr

def insertion_sort(arr, start, end):
    # эта функция делает insertion sort внутри массива
    for i in range(start + 1, end):
        key = arr[i]
        j = i - 1
        while j >= start and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, start, mid, end):
    # а эта - мерджит 2 таких участка
    # !! неопределённое поведение при неотсортированных участках
    left = arr[start:mid].copy()
    right = arr[mid:end].copy()

    i = j = 0
    k = start

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


############ Для сравнения простой merge_sort

def merge_sort(arr):
    l = len(arr)
    if l <= 1:
        return arr # если один элемент - то готово
    else:
        hl = int(l/2)
        left = merge_sort(arr[:hl])
        right = merge_sort(arr[hl:]) # делим на половины и мерджим
        out = []
        l_count, r_count = hl, l-hl
        l_pointer = 0
        r_pointer = 0
        while l_pointer < l_count or r_pointer < r_count:
            if r_pointer < r_count and (l_pointer == l_count or left[l_pointer] > right[r_pointer]):
                out.append(right[r_pointer])
                r_pointer += 1
            else:
                out.append(left[l_pointer])
                l_pointer += 1
        return out

def check_sorted(arr):
    pr = arr[0]
    for i in arr:
        if i < pr:
            print(i, arr[i], pr)
            return False
    return True


a = [1,2,3,4,5,6,54,78,100,1,12,45]
random.shuffle(a)
oarr = [i for i in range(10**5)]
rarr = [random.randint(1,10**6) for i in range(10**5)]
small_rarr = [random.randint(1,10**6) for i in range(10**3)]
timsorted = timsort(rarr)
mergesorted = merge_sort(rarr)

print(rarr)
print(timsorted) # вывод получается очень длинный, но данные сортируются хорошо и быстро
print(mergesorted)

assert check_sorted(timsorted)
assert check_sorted(mergesorted)
print("Массивы отсортированы корректно")

print("\nМаленький случайный массив")
time = timeit.timeit(lambda: timsort(small_rarr), number=100)
print(f"Время Tim: {time:.6f} сек")
time = timeit.timeit(lambda: merge_sort(small_rarr), number=100) # дольше почти в 2 раза
print(f"Время Merge: {time:.6f} сек")
time = timeit.timeit(lambda: sorted(small_rarr), number=100)
print(f"Время sorted: {time:.6f} сек") # быстрее так как написан на си

print("\nБольшой упорядоченный массив")
time = timeit.timeit(lambda: timsort(oarr), number=10)
print(f"Время Tim: {time:.6f} сек")
time = timeit.timeit(lambda: merge_sort(oarr), number=10) # дольше почти в 2 раза
print(f"Время Merge: {time:.6f} сек")
time = timeit.timeit(lambda: sorted(oarr), number=10)
print(f"Время sorted: {time:.6f} сек") # быстрее так как написан на си

print("\nБольшой случайный массив")
time = timeit.timeit(lambda: timsort(rarr), number=10)
print(f"Время Tim: {time:.6f} сек")
time = timeit.timeit(lambda: merge_sort(rarr), number=10) # дольше почти в 2 раза
print(f"Время Merge: {time:.6f} сек")
time = timeit.timeit(lambda: sorted(rarr), number=10)
print(f"Время sorted: {time:.6f} сек") # быстрее так как написан на си

# Выводы:
# Я выбрал именно Timsort, потому что его не просто так
# используют в языках программирования
# Он - удобная комбинация insertion для малого масштаба и merge для большого
# Тесты показали, что он работает быстрее чем merge sort,
# превосходит его в разы
# Сравнивать с sorted некорректно, ибо sorted внутри написан на Си.
#
#
#
# Было интересно выполнить это задание,
# надеюсь оно будет не последним, что я сделаю с командой Lesta Games
#
#
#
#
#
#
