# На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO.
# Объяснить плюсы и минусы каждой реализации.

from task2queues import FIFOlist
from task2queues import FIFOdeque
from task2queues import FIFOLinkedList


# в этом файле у меня только тесты, реализации ищите в папке task2queues

def test_logic():
    print("\n\n== INITIAL LOGIC TEST ==")
    buf = FIFOlist.FIFOlist(3) # привет питону и его random.random()
    print("Add A, B, C:")
    buf.enqueue('A')
    buf.enqueue('B')
    buf.enqueue('C')
    print(f"head: {buf.head}, tail: {buf.tail}")
    buf.print_info()
    # A, B, C

    print("\nAdd D (have to replace A):")
    buf.enqueue('D')
    print(f"head: {buf.head}, tail: {buf.tail}")
    buf.print_info()
    # B, C, D

    print("\nDequeue an item:")
    print(f"Dequeue: {buf.dequeue()}")
    print(f"head: {buf.head}, tail: {buf.tail}")
    buf.print_info()
    # C, D,

    buf.dequeue()
    buf.dequeue()
    buf.print_info() # пусто

def test_errors(throw=False): # вызывает Index Error при throw = True
    print("\n== ERROR TEST ==")
    buf = FIFOlist.FIFOlist(5)
    buf.enqueue("A")
    buf.enqueue("B")
    buf.enqueue("C")
    buf.enqueue("D")
    buf.enqueue("E")
    buf.print_info() # полный
    buf.enqueue("F")
    buf.enqueue("G")
    buf.enqueue("D")
    buf.print_info() # переписали
    for i in range(5):
        buf.dequeue()
    buf.print_info() # пусто

    if throw:
        buf.dequeue()


def test_special_values():
    print("=== PECULIAR VALUES ===")
    buf = FIFOlist.FIFOlist(3)

    buf.enqueue(None)  # None как значение
    buf.enqueue(0)
    buf.enqueue("")
    buf.print_info() # ну пустая строка и выведена

    buf.enqueue("new")  # вытеснит None
    buf.print_info()


def test_single_element():
    print("\n=== ONE ELEMENT BUFFER ===")
    buf = FIFOlist.FIFOlist(1)

    buf.enqueue("alone")
    buf.print_info()  # alone

    buf.enqueue("new")  # Вытеснит alone
    buf.print_info()  # new

    buf.dequeue()
    buf.print_info()  # empty


# это всё тесты для FIFOlist. Для других вариантов будет не так подробно
test_logic()
test_errors()
test_special_values()
test_single_element()

print("\n === NOW DEQUE ===")
buf = FIFOdeque.FIFOdeque(10)
print(buf)

for i in range(10):
    buf.enqueue(chr(ord("A")+i))
    print(buf)

buf.dequeue()
buf.dequeue()
buf.dequeue()

print(buf)

for i in range(5):
    buf.enqueue(chr(ord("А")+i)) # здесь, для различия, русские буквы
    print(buf) # старые элементы уходят

# теперь двусвязный
print("\n\n Linked List test have begun")
print("=== TEST 1: Basic operations ===")
buf = FIFOLinkedList.FIFOLinkedList(3)
print("Created buffer with capacity 3")

print("\nAdding A, B, C:")
buf.enqueue('A')
buf.enqueue('B')
buf.enqueue('C')
buf.print_info()

print("Checking states:")
print(f"Empty? {buf.is_empty()}")
print(f"Full? {buf.is_full()}")

print("\n=== TEST 2: Overwrite ===")
print("Adding D (should overwrite A):")
buf.enqueue('D')
buf.print_info()

print("Extracting elements:")
print(f"Extracted: {buf.dequeue()}")
print(f"Extracted: {buf.dequeue()}")
buf.print_info()

print("\n=== TEST 3: Circular behavior ===")
print("Adding E, F:")
buf.enqueue('E')
buf.enqueue('F')
buf.print_info()

print("Extracting everything:")
while not buf.is_empty():
    print(f"Extracted: {buf.dequeue()}")
print("Now buffer is empty:")
buf.print_info()

print("\n=== TEST 4: Resize increase ===")
small_buf = FIFOLinkedList.FIFOLinkedList(2)
small_buf.enqueue('X')
small_buf.enqueue('Y')
print("Before resize:")
small_buf.print_info()

small_buf.resize(4)
print("After increasing to 4:")
small_buf.print_info()

print("Adding Z, W:")
small_buf.enqueue('Z')
small_buf.enqueue('W')
small_buf.print_info()

print("\n=== TEST 5: Resize decrease ===")
big_buf = FIFOLinkedList.FIFOLinkedList(5)
for i in range(5):
    big_buf.enqueue(i)
print("Before decrease:")
big_buf.print_info()

big_buf.resize(2)
print("After decreasing to 2 (should keep 2 newest elements):")
big_buf.print_info()

print("\n=== TEST 6: Error handling ===")
empty_buf = FIFOLinkedList.FIFOLinkedList(2)
print("Trying to extract from empty buffer:")
try:
    empty_buf.dequeue()
except IndexError as e:
    print(f"Caught error: {e}")

print("\n=== TEST 7: Edge case - buffer with size 1 ===")
tiny_buf = FIFOLinkedList.FIFOLinkedList(1)
tiny_buf.enqueue("only_one")
print("Buffer with 1 element:")
tiny_buf.print_info()

print("Adding new element (should overwrite):")
tiny_buf.enqueue("new_one")
tiny_buf.print_info()

print("Extracting:")
print(f"Extracted: {tiny_buf.dequeue()}")
print("Now empty:")
tiny_buf.print_info()

print("\n All tests completed!")