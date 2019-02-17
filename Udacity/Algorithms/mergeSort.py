"""
take a big array and split it down as much as possible
put it back together and sort all part of it
called Divide and Conquer
[8,3,1,7,0,10,2]
[8][1,3][0,7][2,10] 3 comparisons -> only arrays of size 2 and 1 size on the left
[1,3,8][0,2,7,10] 5 comparisons
[0,1,2,3,7,,8,10]  6
---
efficiency
n-1 comparisons-> n is size of array being built
O(#comparions per step * # steps)
O(nlog(n)) -> always better than bubbleSort
auxillary space = O(n) -> due to copying stuff into arrays

"""
def mergeSort(list):
    print("Splitting", list)
    if len(list) > 1:
        mid = len(list)//2
        left_half = list[:mid]
        right_half = list[mid:]

        mergeSort(left_half)
        mergeSort(right_half)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                list[k] = left_half[i]
                i += 1
            else:
                list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            list[k] = right_half[j]
            j += 1
            k += 1
        print("Merging", list)

list = [54,26,93,17,77,31,44,55,20]
mergeSort(list)
print(list)
