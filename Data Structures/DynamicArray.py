import ctypes

class DynamicArray(object):
    '''
    DYNAMIC ARRAY CLASS (Similar to Python List)
    '''

    def __init__(self):
        self.len = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        '''
        Returns the number of elements sorted in array
        '''
        return self.n

    def __getitem__(self, k):
        '''
        Return element at index k
        '''
        if not 0 <= k < self.n:
            # Checks if k index is in bounds in the array
            return IndexError("Ur shit is out of bounds")

        return self.A[k]

    def append(self, element):
        '''
        Adds element to the end of the array
        '''

        if self.n == self.capacity:
            # Double the capacity if not enough room
            self._resize(2 * self.capacity)

        self.A[self.n] = element
        self.n += 1

    def insertAt(self, item, index):
        '''
        This function inserts the item at any specified index.
        '''

        if index < 0 or index > self.n:
            print("Please give valid index")
            return
        
        if self.n == self.capacity:
            self._resize(2 * self.capacity)
        
        for i in range(self.n-1, index - 1, -1):
            self.A[i + 1] = self.A[i]

        self.A[index] = item
        self.n += 1


    def delete(self):
        '''
        This function deletes item from the end of array
        '''

        if self.n == 0:
            print("Array is empty deletion not possible")
            return

        self.A[self.n-1] = 0
        self.n -= 1


    def removeAt(self, index):
        '''
        This function deletes item from a specified index
        '''

        if self.n == 0:
            print('Array is empty deletion is not possible')
            return
        
        if index < 0  or index >= self.n:
            return IndexError("Deletion not possible... Out of bounds")

        if index == self.n - 1:
            self.A[index] = 0
            self.n -= 1
            return

        for i in range(index, self.n - 1):
            self.A[i] = self.A[i + 1]
        
        self.A[self.n - 1] = 0
        self.n -= 1


    def _resize(self, new_cap):
        '''
        Resize internal array to capacity new_cap
        '''

        B = self.make_array(new_cap)

        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_cap

    
    def make_array(self, new_cap):
        '''
        Returns a new array with new_cap capacity
        '''

        return (new_cap * ctypes_py_object)()

