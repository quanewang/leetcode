"""
2 8 5 3 9 1

ith node
* children: 2i+1, 2i+2
* parent: (i-1)//2

"""


def heapify(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(i, 0, -1):
            k = (j-1)//2
            if a[k]<a[j]:
                swap(a, k, j)
        swap(a, 0, i)
    return a


def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

print(heapify([2, 8, 5, 3, 9, 1]))