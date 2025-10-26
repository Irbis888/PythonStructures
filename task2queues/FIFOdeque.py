from collections import deque


class FIFOdeque:
    # Самая эффективная реализация - использует встроенный deque
    # это не так честно, поэтому потом ещё одну сделаю

    def __init__(self, capacity=100):
        self.capacity = capacity
        self._buffer = deque(maxlen=capacity)

    def enqueue(self, value):
        self._buffer.append(value) # Автоматически вытесняет старые элементы при переполнении

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Buffer is empty")
        return self._buffer.popleft()

    def is_empty(self) -> bool:
        return len(self._buffer) == 0

    def is_full(self) -> bool:
        return len(self._buffer) == self.capacity

    def __len__(self) -> int:
        return len(self._buffer)

    def __str__(self) -> str:
        return f"FIFOdeque({list(self._buffer)})"