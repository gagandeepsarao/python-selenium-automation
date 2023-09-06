#Task 1
#Two Lowest Elements

def find_two_lowest(arr: list):
    arr.sort()
    return arr[0], arr[1]

arr = [198, 3, 4, 9, 10, 9, 2]
a, b = find_two_lowest(arr)
print(a)
print(b)

#Task 2
def invert_list(arr: list):
# Loop through each index of the array
    inversed_list = []
    for i in arr:
        negative_num = i * -1
        inversed_list.append(negative_num)
    return inversed_list

a = [1, 5, -2, 4]
print(invert_list(a))

#Task3

def max_diff(arr: list):
    # Check if the list is empty
    # If it is, return 0 as there's no difference to be calculated
    if len(arr) == 0:
        return 0
# Sort the list in ascending order
    arr.sort()
# After sorting, the smallest element will be at index 0,
    smallest = arr[0]
# and the largest will be at the last index
    largest = arr[-1]
# Calculate and return the difference between the largest and smallest elements
    diff = largest - smallest
# Use indexes of the elements
    return diff

arr = [3, 5, 10, 1]
print(max_diff(arr))

#Task4

def count_larger_neighbors(arr: list):

 # Initialize a variable 'count' to 0. This variable will keep track of the number of elements
# that are larger than both their adjacent neighbors.
    count = 0

# Loop through the list from index 1 to len(arr) - 2. We skip the first and the last elements
# because they don't have both left and right neighbors.
    for i in range(1, len(arr) - 1):

# Check if the current element (arr[i]) is greater than its left neighbor (arr[i - 1])
# and its right neighbor (arr[i + 1]).
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            count += 1
    return count

arr=  [2, 56, 7, 21, 22, 19, 26]
print(count_larger_neighbors(arr))

#Task5

def subtract_min(arr: list):
# Find the minimum element in the list using the 'min' function and store it in 'min_element'.
    min_element = min(arr)
    result = []
    for i in arr:
        ele = i - min_element
        result.append(ele)
    return result

arr = [9, 2, 5, 4, 7, 6, 1]
print(subtract_min(arr))








