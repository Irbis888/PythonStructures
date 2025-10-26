# На языке Python написать алгоритм (функцию) определения четности целого числа,
# который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути.
# Объяснить плюсы и минусы обеих реализаций.

import timeit

# task 1
# это стандартная реализация из условия
def isEvenStandard(value: int) -> bool:
    return value % 2 == 0

# это моя реализация проверки через битмаску
# тут я задумался, не начнёт ли питон проверять каждый бит числа value & 1
# хотя достаточно проверить лишь последний
# в любой случае, битовые операции сильно быстрее поиска остатка
def isEven (value: int) -> bool:
    return value & 1 == 0

# проверим правильность работы
test_limit = 10**6
even = True # это будем менять каждую итерацию
for i in range(test_limit):
    assert isEven(i) == even
    assert isEven(-i) == even
    even = not even
print(f"Тесты пройдены успешно для чисел до {test_limit} по модулю")
# в целом можно было проверить для одного чётного и одного нечётного, но кто мне запретит проверить до 10**6?

print(isEven(0))
print(isEven(3))
print(isEven(2))
print(isEven(-1))
print(isEven(-20))
# True, False, True, False, True

# проверка быстродействия через timeit, везде по 100000 повторений
small_number, big_number, large_number, monstrous_number, negative_monster = \
    123, 123456789101112, 2**100, 2**10000*(3**150)+1, -2**10000*(3**150)+1
print("\nПобитовое И")
time = timeit.timeit(lambda: isEven(small_number), number=100000)
print(f"Время: {time:.6f} сек")
time = timeit.timeit(lambda: isEven(big_number), number=100000)
print(f"Время: {time:.6f} сек")
time = timeit.timeit(lambda: isEven(large_number), number=100000)
print(f"Время: {time:.6f} сек")
time = timeit.timeit(lambda: isEven(monstrous_number), number=100000) # Время: ~0.018831 сек
print(f"Время: {time:.6f} сек")
time = timeit.timeit(lambda: isEven(negative_monster), number=100000)
print(f"Время: {time:.6f} сек")

print("\nДеление с остатком")
# для сравнения, стандартная реализация
time = timeit.timeit(lambda: isEvenStandard(small_number), number=100000)
print(f"Время: {time:.6f} сек")
time = timeit.timeit(lambda: isEvenStandard(big_number), number=100000)
print(f"Время: {time:.6f} сек")
time = timeit.timeit(lambda: isEvenStandard(large_number), number=100000)
print(f"Время: {time:.6f} сек")
time = timeit.timeit(lambda: isEvenStandard(monstrous_number), number=100000) # Время: ~0.360977 сек
print(f"Время: {time:.6f} сек")
time = timeit.timeit(lambda: isEvenStandard(negative_monster), number=100000)
print(f"Время: {time:.6f} сек")

# из тестов видно, что на огромных числах остаток от деления
# тратит в десятки раз больше времени

# Преимущества побитового И:
# + не зависит от длины числа, всегда работает с одной скоростью
# + скорость в целом быстрее чем при взятии остатка

# Недостатки побитового И:
# - скорость уменьшается при отрицательном аргументе
# (в более низкоуровневом языке можно было бы от этого избавиться)


# Преимущества проверки остатка:
# + универсально, позволяет проверять делимость не только на степени двойки
# + понятно при чтении кода
# не вызывает исключения при вызове с дробным аргументом
# (isEven(2.0) даёт ошибку, isEvenStandard(2.0) работает корректно)



# Здесь задачу 1 считаю исчерпанной







