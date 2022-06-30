'''
The merge sort algorithm is a sorting alg. that is considered as an example of the divide
and conquer strategy. The array is initially divided into two equal halves and then they are
combined in a sorted manner... We can think of it as a recursive alg.. that continously splits the array
in half until it cannot be divided further. This means that if the array becomes empty or has only one
element left... the dividing will stop. It is the base case to stop the recursion.

Pseudocode: 
    - declare left variable to 0 and right var to n - 1
    - find mid by medium formula... mid = (left + right) / 2
    - call merge sort on (left, mid)
    - call merge sort on (mid + 1, right)
    - continue till left is less than right
    - then call merge function to perform merge sort.

Time Complexity: O(nlog(n))
'''

def mergeSort(arr):
    if len(arr) > 1:


        #finding the mid of the array
        mid = len(arr) // 2

        #diving the array elements
        left = arr[:mid]
        right = arr[mid:]

        #sorting the first half
        mergeSort(left)

        #sorting the second half
        mergeSort(right)

        i = j = k = 0

        #copy data to temporary arrays left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        #checking if any element was left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 6]

    mergeSort(arr)

    print(arr)
    
