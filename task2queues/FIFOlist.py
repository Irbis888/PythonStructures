# Здесь я реализую наивную очередь через список
# конечной фиксированной длины
class FIFOlist:
    head: int
    tail: int
    size: int
    capacity: int
    # характеристики буффера

    def __init__(self, capacity: int = 100):
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0
        self.capacity = capacity

    def enqueue(self, value):
        if self.is_full():
            self.head = (self.head + 1) % self.capacity
            # в случае полного буфера перезаписываем голову
            # можно было выдавать ошибку, но так неинтересно
            self.size -= 1
            print("warning: overwritten head")

        self.buffer[self.tail] = value
        self.size += 1
        self.tail = (self.tail + 1) % self.capacity


    def dequeue(self):
        if self.is_empty():
            raise IndexError("Buffer is empty")

        value = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return value  # тут сохраним то, что только что достали

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def print_info(self): # тут функция для вывода информации за одно обращение
        i = self.head
        # print(f"Capacity: {self.capacity}")
        # Сначала выводил capacity, потом решил что не надо т. к. это константа
        print(f"Size: {self.size}")  # здесь начал писать в print на английском, решил и дальше так
        print("Contents: ")
        if self.is_empty():
            print("Buffer is empty")
        if self.is_full():
            print(self.buffer[i], end=", ")
            i = (i + 1) % self.capacity
        while i != self.tail:  # выводим от головы к хвосту
            print(self.buffer[i], end=", ")
            i = (i + 1) % self.capacity
        print()