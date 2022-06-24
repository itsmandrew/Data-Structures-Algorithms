class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None


    def print_list(self):
        '''
        Prints out the entire linked list.
        '''
        print_val = self.head
        while print_val != None:
            print(print_val.data, end = " -> ")
            print_val = print_val.next

        print("NULL")

    def addToBeginning(self, new_data):
        '''
        Parameter takes data for the new node.
        Adds new node to the beginning of the linked list
        '''
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node

    def addToEnd(self, new_data):
        '''
        Parameter takes data for the new node.
        Adds new node to the end of the linked list
        '''

        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        
        prev = self.head

        while (prev.next):
            prev = prev.next
        
        prev.next = new_node
    
    def insertBetween(self, destination, new_data):
        '''
        Inserts new node after the desired node
        '''
        if destination is None:
            print("This node doesn't exist")
            return
        
        new_node = Node(new_data)
        new_node.next = destination.next
        destination.next = new_node

    def removeNode(self, removeData):
        '''
        Removes the node, given the data that matches the node's data
        '''
        #stores head node
        head = self.head

        # if head node itself holds the key to be deleted
        if (head != None):
            if (head.data == removeData):
                self.head = head.next
                head = None
                return
        
        #search for the key to be deleted, keep track f the prev node
        #as we need to change prev.next
        while (head != None):
            if head.data == removeData:
                break
            prev = head
            head = head.next

        #if key was not present in linked list
        if (head == None):
            print("Value not found")
            return
        
        #unlink the node from linked list
        prev.next = head.next
        head = None

    def getCount(self):
        '''
        Deadass just returns the length of the linked list
        '''

        temp = self.head
        count = 0

        while (temp != None):
            count += 1
            temp = temp.next

        return count



if __name__ == "__main__":
    list1 = SLinkedList()
    list1.head = Node("First Element")

    list1.addToEnd(2)
    list1.addToBeginning(3)

    list1.print_list()
    print(list1.getCount())