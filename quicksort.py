def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


# Test it
if __name__ == "__main__":
    test = [3, 6, 8, 10, 1, 2, 1]
    print(f"Original: {test}")
    print(f"Sorted:   {quicksort(test)}")
