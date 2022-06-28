'''
Bubble sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements
if they are in the wrong order. This is not suitable for large data sets as its average and worst case time
complexity is quite high

Time complexity = O(n^2)

It is popular for its capability to detect a very small error in almost-sorted array and fix it with just linear
complexity (2n)
'''

def bubbleSort(array):
    n = len(array)

    og_arr = array[:]
    arr = array[:]
    #Traverse through all array elements

    for i in range(n):
        swapped = False

        #Last i elements are already in place
        for j in range(0, n - i - 1):

            #Traverse the array from 0 to n - i - 1.
            #Swap if the element found is greater than the next element

            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        #IF NO TWO ELEMENTS WERE SWAPPED
        #BY INNER LOOP, THEN BREAK
        #The algorithm needs one whole pass w/o any swaps to know it is sorted
        if swapped == False:
            break

    print(f'Original Array: {og_arr}')
    print(f'Sorted Array: {arr}')



if __name__ == "__main__":

    a = [64, 32, 25, 12, 22, 11, 90]

    bubbleSort(a)