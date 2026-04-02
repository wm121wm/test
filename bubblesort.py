#开始写一个冒泡排序（优化版）
def bubble_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    for i in range(n):
        swapped = False
        # 优化：每轮最后交换位置之后的元素已经是有序的
        # 优化：提前终止，如果一轮没有交换说明已排序完成
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
#继续写测试例
if __name__ == "__main__":
    test = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {test}")
    print(f"Sorted:   {bubble_sort(test)}")
