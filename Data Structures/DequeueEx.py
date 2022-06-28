#Python program to demonstrate queue implementation using
#collections.queue

#PYTHON HAS A BUILT IN FOR A DOUBLE ENDED QUEUE... XD
from collections import deque

# Initializing a queue
q = deque()

q.append('a')
q.append('b')
q.append('c')

print("Initial queue")
print(q)

print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)


