class Stack:
    """Simple stack implementation using list."""

    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if not self._items:
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)


if __name__ == "__main__":
    # Simple demonstration
    s = Stack()
    s.push(1)
    s.push(2)
    print("Stack top:", s.peek())
    print("Stack size:", s.size())
    print("Pop:", s.pop())
    print("Stack empty:", s.is_empty())
