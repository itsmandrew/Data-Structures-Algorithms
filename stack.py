class Stack:

    def __init__(self):
        self.stack = []
        self.count = 0

    def __str__(self):
        
        out = ""

        if self.count == 0:
            out = "STACK IS EMPTY"
            return out

        else:

            for x in range(len(self.stack) - 1, -1, -1):
                out += "+-------+\n"
                out += f'|   {self.stack[x]}   |\n'

            return out


    def push(self, value):
        '''
        Adds value to the top of the stack
        '''
        self.stack.append(value)
        self.count += 1

    def pop(self):
        '''
        Deletes the top element of the stack
        '''
        if self.isEmpty():
            raise Exception("Dude stop... your popping from an empty stack")

        self.stack.pop()
        self.count -= 1

    def getSize(self):
        '''
        Returns the size of the stack
        '''
        return self.count


    def isEmpty(self):
        '''
        Checks if the stack is empty
        '''

        return self.count == 0
    
if __name__ == "__main__":
    stack = Stack()
    
    for x in range(0, 5):
        stack.push(x)

    stack.pop()
    stack.pop()
    stack.push(7)
    stack.pop()
    stack.push(4)
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()

    stack.push(1)
    stack.push(3)
    stack.pop()
    stack.pop()
    stack.push(3)
    stack.push(4)
    stack.pop()
    print(stack)