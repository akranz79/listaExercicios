class Stack:
    def __init__(self, capacity=30):
        self.pool = []
        self.capacity = capacity

    def clear(self):
        self.pool.clear()

    def isEmpty(self):
        return len(self.pool) == 0

    def topEl(self):
        return self.pool[-1]

    def pop(self):
        el = self.pool.pop()
        return el

    def push(self, el):
        if len(self.pool) < self.capacity:
            self.pool.append(el)
        else:
            print("Stack overflow! Cannot push element:", el)

# Exemplo de uso
if __name__ == "__main__":
    stack = Stack()

    print("Is empty?", stack.isEmpty())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Top element:", stack.topEl())
    print("Pop element:", stack.pop())
    print("Top element after pop:", stack.topEl())

    print("Is empty?", stack.isEmpty())

    stack.clear()
    print("Is empty after clear?", stack.isEmpty())
