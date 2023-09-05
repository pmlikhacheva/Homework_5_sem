#быстрая сортировка Хоара
def hoar_sort(A, depth=1, part='left'):
    print('depth:', depth, 'part:', part, 'array before:', A)
    if len(A) <= 1:
        return A
    l = []
    r = []
    m = []
    barrier = A[0]
    for i in range(0, len(A), 1):
        if A[i] < barrier:
            l.append(A[i])
        if A[i] > barrier:
            r.append(A[i])
        if A[i] == barrier:
            m.append(A[i])
    A.clear()
    A = hoar_sort(l, depth + 1, part = "left") + m + hoar_sort(r, depth + 1, part = "right")

    print('depth:', depth, 'part:', part, 'array after:', A)
    return A
