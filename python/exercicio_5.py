class LLStack:
    def __init__(self):
        self.lst = []

    def clear(self):
        self.lst.clear()

    def isEmpty(self):
        return len(self.lst) == 0

    def topEl(self):
        return self.lst[-1]

    def pop(self):
        el = self.lst.pop()
        return el

    def push(self, el):
        self.lst.append(el)

# Exemplo de uso
if __name__ == "__main__":
    stack = LLStack()

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
