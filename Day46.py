def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

# Example usage:
lst = [1, 3, 5, 7, 9]
if is_sorted(lst):
    print("The list is sorted.")
else:
    print("The list is not sorted.")
