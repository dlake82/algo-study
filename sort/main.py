import numpy as np
import time


def make_seed_and_sort(sort_name):
    np.random.seed(int(time.time()))
    arr = [6, 5, 3, 1, 8, 7, 2, 4]
    start = time.time()
    form = "%M분 %S초"
    print(sort_name + f"\n시작시간: {time.strftime(form, time.localtime(start))}")
    print(arr)
    arr = eval(sort_name + "(arr)")
    print(f"걸린시간: {float(time.time() - start):0.10}")
    print(arr, "\n")

def bubble_sort(arr):
    for i in range(1, len(arr)):
        for j in range(len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        index = i
        for j in range(i + 1, len(arr)):
            if arr[index] > arr[j]:
                index = j
        arr[i], arr[index] = arr[index], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while arr[j] > temp and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    return arr

def qsort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left, right = [], []
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return qsort(left) + [pivot] + qsort(right)

def merge_sort(arr):
    def sort(start, end):
        if end - start < 2:
            return arr
        mid = (start + end) // 2
        sort(start, mid)
        sort(mid, end)
        mereg(start, mid, end)

    def merge(start, mid, end):
        temp = []
        a, b = start, mid
        while a < start and b < end:
            if arr[a] < arr[b]:
                temp.append(arr[a])
                a += 1
            else:
                temp.append(arr[b])
                b += 1
        while a < mid:
            temp.append(arr[a])
            a += 1
        while b < end:
            temp.append(arr[b])
            b += 1

        for i in range(start, end):
            arr[i] = temp[i - start]
        return temp
    return sort(0, len(arr))


make_seed_and_sort("bubble_sort")
make_seed_and_sort("selection_sort")
make_seed_and_sort("insertion_sort")
make_seed_and_sort("qsort")
make_seed_and_sort("merge_sort")
