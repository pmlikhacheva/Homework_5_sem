#пирамидальная сортировка Heap Sort
def insert(heap, a):
    heap.append(a)
    i = len(heap) - 1
    while (i - 1) // 2 >= 0:
        if heap[i] >= heap[(i - 1)//2]:
            heap[(i - 1) // 2], heap[i] = heap[i], heap[(i - 1) // 2]
        i = (i - 1) // 2

    return heap

def create_max_heap(arr):
    heap = list()
    for a in arr:
        heap = insert(heap, a)
    return heap

def heapsort(arr):
    arr = create_max_heap(arr)
    n = len(arr)
    for i in range(0, n - 1):
        arr[0], arr[n - i - 1] = arr[n - i - 1], arr[0]
        arr = create_max_heap(arr[:(n - i - 1)]) + arr[(n - i - 1):]
    return arr

A = input().split()
B = [1, 6, 24, 14, 5, 2]
print(*heapsort(B))
