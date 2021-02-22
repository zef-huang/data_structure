# coding=utf8

# ------------------------------------------------------
# 1. 二分查找算法
# ------------------------------------------------------

def bi_search(arr, num):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right)//2

        if num > arr[mid]:
            left = mid + 1
        elif num < arr[mid]:
            right = mid - 1
        else:
            return mid

    return -1 


if __name__ == '__main__':
    index = bi_search([1, 4, 6, 8, 12, 34, 66], 11)
    print(index)
