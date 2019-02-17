"""
pick a random value in the array
pick a random value -> pivot
move all value large above and all values lower below it
pick a pivot within the upper and lower bounds -> do the same thing
[8,3,1,7,0,10,2] -> 2 is pivot
[10,3,1,7,0,2,8] -> 2 goes one left, 10 goes to front,
[0,3,1,7,2,10,8] -> move only if larger

---
efficiency
worst case: O(n^2)
pivot is biggest and end of array
next pivot is also biggest
best and average case: O(nlogn) -> similar to mergeSort
optimizations to run faster:
can run both halves at the same time, can also select median
as the pivot
Space: O(n)
"""
def quicksort(array):
    less = []
    equal = []
    greater = []
    n = len(array)//2
    if len(array) > 1:
        pivot = array[n]

        for i in array:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                equal.append(i)
            elif i > pivot:
                greater.append(i)
        return quicksort(less) + equal + quicksort(greater)
    else:
        return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)
