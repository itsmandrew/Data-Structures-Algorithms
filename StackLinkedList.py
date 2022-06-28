#Python program to demonstack stacks
#stack implementation using a linked list...


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class StackLinkedList:

    def __init__(self):
        '''
        Initializing a stack
        Uses a dummy node, which is easier for handling edge cases.
        '''
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        '''
        String representation of the stack
        This is what will show up when we print("stack")
        '''
        curr = self.head.next
        out = ""

        while curr:
            out += str(curr.value) + " -> "
            curr = curr.next

        return out[:-4]


    def getSize(self):
        '''
        Returns the number of elements in the stack
        '''
        return self.size

    def isEmpty(self):
        '''
        Checks if the stack is empty
        '''
        return self.size == 0

    
    def peek(self):
        '''
        Gets the top item of the stack
        '''
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        
        return self.head.next.value

    
    def push(self, value):
        '''
        Pushes value to the top of the stack
        '''
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        '''
        Removes value from the top of the stack
        and returns the value
        '''
        if self.isEmpty():
            raise Exception('Popping from an empty stack')
        
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value


if __name__ == "__main__":
    stack = StackLinkedList()

    for i in range(1, 11):
        stack.push(i)
    
    print(stack)
