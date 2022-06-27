import gc

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    
    def __init__(self):
        self.head = None

    
    def push(self, new_data):

        #steps 1 and 2: Allocates new node and puts in the data
        new_node = Node(new_data)

        #step 3: make next of new node as head and previous as NULL
        new_node.next = self.head
        new_node.prev = None

        #step 4: change prev of head node to new node
        if self.head != None:
            self.head.prev = new_node

        #step 5: move the head to point to the new node
        self.head = new_node

    def insertAfter(self, prev_node, new_data):

        #1.) checks if the the given prev_node is NULL
        if prev_node == None:
            return

        #2.) Allocates node and 3.) puts in the data for new node
        new_node = Node(new_data)

        #4.) Make next of new node as next of prev_node
        new_node.next = prev_node.next

        #5.) Make the next of prev_node as new_node
        prev_node.next = new_node

        #6.) Makes the prev_node as previous of new_node
        new_node.prev = prev_node

        #7.) Change previous new_node's next node */
        if new_node.next != None:
            new_node.next.prev = new_node

    
    def print_list(self):
        
        temp = self.head
        while temp != None:
            print(temp.data, end = ' <-> ')
            last = temp
            temp = temp.next

        print("NULL")

    def append(self, new_data):

        #1.) Allocate node 2.) Put in the data
        new_node = Node(new_data)

        #3.) Since this node is going to be the last node... make the .next == None
        #PS... it is already initialized as None

        #4.) If the linked list is empty, then make the new node as head
        if self.head == None:
            self.head = new_node
            return
        
        #5.) Else... traverse the list till the last node
        last = self.head
        while last.next:
            last = last.next

        #6.) Change the next of last node
        last.next = new_node

        #7.) Make last node as previous of new node
        new_node.prev = last
        return

    def deleteNode(self, key):

        #Base case
        if self.head == None or key == None:
            return
        
        #If node to be deleted is head node
        if self.head == key:
            self.head = key.next
    
        #Change next only if node to be deleted is NOT the last node
        if key.next != None:
            key.next.prev = key.prev
        
        #change prev only if node to be deleted is NOT the first node
        if key.prev != None:
            key.prev.next = key.next
        
        gc.collect()

    def deleteNodeAtIndex(self, n):
        
        #if list is None or invalid position is given
        if (self.head == None or n <= 0):
            print("Index DNE... pick something greater than 0")
            return

        curr = self.head
        count = 1

        #traverse up to the node at position "count" from the beginning
        while (curr != None and count < n):
            curr = curr.next
            count += 1

        #if "count" is greater than the number of nodes in the doubly linked list
        if (curr == None):
            return

        self.deleteNode(curr)

    def getCount(self):

        temp = self.head
        count = 0

        while (temp != None):
            count += 1
            temp = temp.next

        return count


if __name__ == "__main__":

    dlist = DoublyLinkedList()
    dlist.push(4)
    dlist.push(6)
    dlist.print_list()

    dlist.deleteNodeAtIndex(0)

    dlist.print_list()
    
    print(dlist.getCount())
