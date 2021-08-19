import sys

class Stack:
    Stack = []
    Stack_size = 0
    def push(self, num):
        self.stack_size += 1
        self.stack.append(num)

    def pop(self, num):
        if self.size > 0:
            self.stack_size -= 1
            return self.Stack.pop(self.Stack_size)

    def size(self):
        return self.Stack_size

    def empty(self):
        if self.Stack_size == 0:
            return 1
        else:
            return 0

    def top(self):
        if self.Stack_size > 0:
            return self.Stack[self.Stack_size-1]
        else:
            return -1

i = int(input())
Stack = Stack()
while i>0:
    i -= 1
    command = sys.stdin.readline().rstrip().split()
    if command[0] == 'push':
        Stack.push(int(command[1]))
    elif command[0] == 'top':
        print(Stack.top)
    elif command[0] == 'size':
        print(Stack.size())
    elif command[0] == 'empty':
        print(Stack.size())
    else:
        print(Stack.pop())




