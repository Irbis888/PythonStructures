# Здесь я сделаю буфер на двусвязном списке
# тут пропадает смысл цикличного буфера так как
# узлы двусвязного списка можно создавать бесконечно
# зато его можно динамически расширять

class Node:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None
        # в списке при создании даже самой первой ноды тут будет не None, а другие ноды
        # или эта же нода, если это первый элемент


class FIFOLinkedList:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.size = 0
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)

        if self.is_empty(): # Если первый элемент - создаём кольцо из него
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
            self.tail = new_node
            self.size = 1
        elif self.is_full():
            self.head = self.head.next
            self.tail = self.tail.next
            self.tail.value = value
        else:
            # Добавляем новый узел после tail
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node
            self.size += 1

    def dequeue(self): # удаляем всегда голову
        if self.is_empty():
            raise IndexError("Buffer is empty")

        value = self.head.value

        if self.size == 1:
            # Последний элемент
            self.head = None
            self.tail = None
            self.size = 0
        else:
            # Удаляем head
            new_head = self.head.next
            new_head.prev = self.head.prev
            self.head.prev.next = new_head
            self.head = new_head
            self.size -= 1

        return value

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def resize(self, new_cap):
        if new_cap <= 0:
            print("Capacity must be positive")
            return
        if new_cap == self.capacity:
            return
        elif new_cap > self.capacity:
            self.capacity = new_cap
        else: # если меньше - выполняется за O(new_cap)
            elements_to_remove = self.size - new_cap
            if elements_to_remove > 0: # если надо че нибудь убирать
                for _ in range(elements_to_remove):
                    self.head = self.head.next
                self.size = new_cap
            self.capacity = new_cap




    def print_info(self): # тут функция для вывода информации за одно обращение
        i = self.head
        print(f"Size: {self.size}")  # здесь начал писать в print на английском, решил и дальше так
        print("Contents: ")
        if self.is_empty():
            print("Buffer is empty")
        for _ in range(self.size):
            print(i.value)
            i = i.next
        print()

# уже после реализации этого шедевра я понял что вместо head и tail можно было держать 1 указатель
# так как head и tail всегда друг за другом
