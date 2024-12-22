from collections import deque
import time
import random


class CircularBufferList:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
      return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Буфер полон")
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Буфер пуст")
        item = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Буфер пуст")
        return self.buffer[self.head]
    

class CircularBufferDeque:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.buffer = deque(maxlen=capacity)

    def is_empty(self) -> bool:
        return len(self.buffer) == 0

    def is_full(self) -> bool:
      return len(self.buffer) == self.capacity

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Буфер полон")
        self.buffer.append(item)


    def dequeue(self):
        if self.is_empty():
            raise IndexError("Буфер пуст")
        return self.buffer.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("Буфер пуст")
        return self.buffer[0]
    


"""
CircularBufferList (использование list):
Плюсы:
Код легко понять
Минусы:
Ручная реализация логики head и tail.
Требуется отслеживание размера.

CircularBufferDeque (использование collections.deque):
Плюсы:
Более эффективна, чем CircularBufferList, особенно при большом кол-ве добавлении/удалении элементов.
Меньше кода, за счет использования deque.
Минусы:
Сложнее в понимании, чем CircularBufferList из-за использования стороннего инструмента.

В среднем время работы с CircularBufferList будет медленее из-за небольших накладных расходов из-за операции self.buffer[self.head] = None
"""