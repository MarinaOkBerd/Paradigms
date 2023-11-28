def binary_search(arr, element):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == element:
            return mid
        elif arr[mid] < element:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = [11, 22, 33, 44, 55, 66]
element = 99
result = binary_search(arr, element)

if result == -1:
    print("-1")
else:
    print(result)

