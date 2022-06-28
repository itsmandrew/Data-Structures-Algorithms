'''
Selection sort sorts an array by repeatedly finding the min element
from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array
'''


'''
-Initialize minimum value (min_idx) to location 0
-Traverse the array to find the min element in the array
-While traversing if any element smaller than min_inx is found then swap both the values
-Then increment min_inx to point to next element
-Repeat until array is sorted...
'''

def selection_sort(array):

    new_arr = array[:]
    og_arr = array[:]

    #traverse through all array elements
    for i in range(len(new_arr)):

        #find the min element in remain unsorted array
        min_index = i

        for j in range(i + 1, len(new_arr)):
            if new_arr[min_index] > new_arr[j]:
                min_index = j

        #Swap the found min element with the first element...
        new_arr[i], new_arr[min_index] = new_arr[min_index], new_arr[i]

    print(f'Original Array: {og_arr}')
    print(f'Sorted Array: {new_arr}')


if __name__ == "__main__":
    a = [64, 25, 12, 22, 11]

    selection_sort(a)
