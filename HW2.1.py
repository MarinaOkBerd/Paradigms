def merge_sort(arr):
    if len(arr) > 1:
        left_half, right_half = get_middle_arr(arr)
        i = j = k = 0
        i, j, k = combaine_arr(arr, i, j, k, left_half, right_half)
        add_half(arr, i, k, left_half)
        add_half(arr, j, k, right_half)

def add_half(arr, j, k, right_half):
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

def get_middle_arr(arr):
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    merge_sort(left_half)
    merge_sort(right_half)
    return left_half, right_half

def combaine_arr(arr, i, j, k, left_half, right_half):
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1
    return i, j, k


my_array = [64, 34, 25, 12, 22, 11, 90]
merge_sort(my_array)
print("Отсортированный массив (Merge Sort):", my_array)