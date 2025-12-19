'''
In Python, the term “in-place” usually means that we modify the same input list and do not use additional data structures like separate arrays.
 However, it does not always imply strictly O(1) auxiliary space. Operations such as list slicing and the sorted() function create new lists internally, 
 which use extra memory. Even list.sort() relies on Timsort, which can consume additional space in certain cases. Conceptually, the algorithm is in-place 
 because the original array is rearranged, but from a strict space-complexity perspective, Python does not guarantee O(1) auxiliary space. For true O(1) 
 space, a lower-level language like C++ with in-place subrange sorting is required.

 “Conceptually it is in-place since we rearrange within the same array, but in Python slicing and sorted() allocate extra memory.
 For strict O(1) auxiliary space, we would need an in-place sorting algorithm or a language like C++ where we can sort subranges without copying.”
'''

def sortIt(self, arr):
    arr.sort()
    n = len(arr)

    i = 0
    j = n - 1

    # Step 1: Partition odds to left, evens to right
    while i <= j:
        if arr[i] % 2 == 1:
            i += 1
        elif arr[j] % 2 == 0:
            j -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    # i now points to first even index
    odd_end = i

    # Step 2: Sort odds (descending)
    arr[:odd_end] = sorted(arr[:odd_end], reverse=True)

    # Step 3: Sort evens (ascending)
    arr[odd_end:] = sorted(arr[odd_end:])
        