class ArrayQueue:
    def __init__(self, size=100):
        self.size = size
        self.first = self.last = -1
        self.storage = [None] * size

    def enqueue(self, el):
        if not self.isFull():
            if self.last == self.size - 1 or self.last == -1:
                self.storage[0] = el
                self.last = 0
                if self.first == -1:
                    self.first = 0
            else:
                self.last += 1
                self.storage[self.last] = el
        else:
            print("Fila cheia.")

    def dequeue(self):
        if not self.isEmpty():
            tmp = self.storage[self.first]
            if self.first == self.last:
                self.last = self.first = -1
            elif self.first == self.size - 1:
                self.first = 0
            else:
                self.first += 1
            return tmp
        else:
            print("Fila vazia.")

    def isFull(self):
        return self.first == 0 and self.last == self.size - 1 or self.first == self.last + 1

    def isEmpty(self):
        return self.first == -1

# Exemplo de uso
if __name__ == "__main__":
    queue = ArrayQueue()

    print("Is empty?", queue.isEmpty())
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Dequeue element:", queue.dequeue())
    print("Dequeue element:", queue.dequeue())
    print("Is empty?", queue.isEmpty())
    queue.enqueue(4)
    queue.enqueue(5)
    print("Is full?", queue.isFull())
    queue.enqueue(6)  # Isso deve imprimir "Fila cheia."
