class QueueArray:

    def __init__(self, c):
        #c is the capacity of the array
        self.queue = []
        self.front = self.rear = 0
        self.capacity = c

    
    def enqueue(self, data):
        '''
        Function to insert an element at the end of the queue
        '''

        if (self.capacity == self.rear):
            print("QUEUE IS FULL")
        
        else:
            self.queue.append(data)
            self.rear += 1

    def dequeue(self):
        '''
        Function to delete an element from the front
        of the queue
        '''

        if (self.front == self.rear):
            print("QUEUE IS EMPTY")

        else:
            self.queue.pop(0)
            self.rear -= 1

    def printQueue(self):
        '''
        Prints the entire queue for display
        '''

        if (self.front == self.rear):
            print("QUEUE IS EMPTY")

        for i in self.queue:
            print(i, "<--", end = " ")
        
        if self.rear != 0:
            print("END")


if __name__ == "__main__":
    q = QueueArray(5)
    q.enqueue(4)
    q.enqueue(3)
    q.enqueue(1)
    q.dequeue()
    q.dequeue()
    q.printQueue()