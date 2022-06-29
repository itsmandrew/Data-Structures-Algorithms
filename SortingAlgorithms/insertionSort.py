'''
Insertion sort is a simple sorting alg. that works similar to the way you
sort playing cards in your hard. The array is virtually split into a sorted
and an unsorted part. Values from the unsorted part are picked and placed at the correct
position in the sorted part.

characteristics of insertion sort:
- the simplest algorithm with simple implementation
- efficient for small data values
- adaptive in nature... it is appropriate for data sets which are already partially sorted

time complexity:  O(n^2)

'''

def insertionSort(array):
    
    og_arr = array[:]
    arr = array[:]

    #Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        
        j = i - 1
        key = arr[i]

        #Compare key with each element on the left of it until an element smaller than it
        #is found.
        #For descending order, change key < array[j]  to key > array[j]
        while j >= 0  and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        
        #Place key at after the element just smaller than it
        arr[j + 1] = key

    print(f'Original Array: {og_arr}')
    print(f'Sorted Array: {arr}')

if __name__ == "__main__":

    a = [12, 11, 13, 17, 5, 6, 17]
    insertionSort(a)
