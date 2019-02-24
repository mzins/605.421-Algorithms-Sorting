import random
import time


def generate_numbers(n):
    return [random.randint(0,1000) for i in range(0,n)]

def merge(left, right):
    merged = []

    while len(left) > 0 and len(right) > 0:
        temp_left = left[0]
        temp_right = right[0]

        if temp_left < temp_right:
            left.pop(0)
            merged.append(temp_left)
        else:
            right.pop(0)
            merged.append(temp_right)

    if len(left) > 0:
        merged = merged + left
    if len(right) > 0:
        merged = merged + right

    return sorted(merged)


def merge_sort(values):
    '''
    MergeSort():
        MergeSortLeft()
        MergeSortRight()
        MergeLeftAndRight()
    :return: sorted list
    '''

    if len(values) == 1:
        return values

    else:
        left = values[:len(values)//2]
        right = values[len(values)//2:]
        left = merge_sort(left)
        right = merge_sort(right)
    return merge(left, right)


def calc_median(numbers):
    sorted = merge_sort(numbers)
    if len(sorted) % 2 == 1:
        return sorted[len(sorted)//2]
    return sorted[len(sorted) // 2 - 1]


def get_run_times():
    with open('mergesort2.csv', 'w') as file:
        for i in range(1, 10000000, 100):
            unsorted = generate_numbers(i)
            start = time.time()
            calc_median(unsorted)
            end = time.time()
            calc_time = end - start
            file.write("{}, {}\n".format(i,calc_time))

get_run_times()