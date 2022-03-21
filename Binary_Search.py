def binary_search(array, search_value):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if search_value == array[mid]:
            return 1
        elif search_value < array[mid]:
            high = mid - 1
        elif search_value > array[mid]:
            low = mid + 1
    return 0


print(binary_search([2, 3, 4, 10, 40, 33], 3))
