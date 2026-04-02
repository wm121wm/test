def heap_sort(arr):
    """堆排序算法"""
    n = len(arr)

    # 构建最大堆
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 逐个提取元素
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


def heapify(arr, n, i):
    """将数组调整为最大堆"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


if __name__ == "__main__":
    # 测试
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", arr)
    sorted_arr = heap_sort(arr)
    print("排序后:", sorted_arr)
