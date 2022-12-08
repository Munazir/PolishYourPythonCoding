# stack


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def size(self):
        return len(self.items)

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    s = Stack()
    print(s.is_empty())
    print(s.size())
    s.push(1)
    s.push(2)
    print(s)
    s.pop()
    print(s)
    s.push(2)
    s.push(3)
    s.push(6)
    print(s)
    print(s.peek())
