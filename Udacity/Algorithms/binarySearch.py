"""
assume list is sorted
start in the middle of the array
check what your target is and what middle value is
if less than search left half
if more search right half

repeat with middle elements

---
Effeciency
even number of elements: err on a side, go left or right
worst case: element that is bigger than anything in array them
err on the lower side
everytime an array doubles, it increases
Effeciency: O(2^x + 1)-> O(log2(n)+1)->O(log(n)) (usual base is 2)
Using a results table can help notice patterns, help think of things

index() -> python searches and returns the first index with that
value -> not too fast
elements need to be in increasing order
"""
def binary_search(input_array, value):
    low = 0
    high = len(input_array) - 1
    while (low <= high):
        middle = (low + high) / 2
        if (input_array[middle] == value):
            return middle
        elif (input_array[middle] < value):
            low = middle + 1
        else:
            high = middle - 1
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
