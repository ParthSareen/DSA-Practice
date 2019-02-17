"""
bubble sort
start at beginning switch to left if smaller - very naive approach
n-1 comparisons, n-1 iterations
(n-1)^2
worst case: O(n^2) = average case
best case: O(n)
space complexity: O(1)
"""
def bubbleSort(list):
    for num in range(len(list)-1,0,-1):
        for i in range(num):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list [i+1]
                list[i+1] = temp
list = [12,34,2,45,6]
bubbleSort(list)
print(list)
