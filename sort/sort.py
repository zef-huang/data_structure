# coding=utf8


# ------------------------------------------------------
# 1. 插入排序
# ------------------------------------------------------


def insert_sort(num_list):
    for i in range(len(num_list)):
        tmp = num_list[i]

        while i > 0:
            before = i - 1
            if tmp < num_list[before]:
                num_list[i] = num_list[before]
                i -= 1
            else:
                break

        num_list[i] = tmp        

    return num_list


# ------------------------------------------------------
# 2. 折半插入排序
# ------------------------------------------------------


def bi_insert_sort(num_list):
    for i in range(len(num_list)):
        tmp = num_list[i]

        left = 0
        right = i - 1
        copy_right = right
        while left <= right:
            mid = (left + right) // 2

            if tmp > num_list[mid]:
                left = mid + 1
            elif tmp < num_list[mid]:
                right = mid - 1
            else:
                break
        
        while copy_right >= left:
            num_list[copy_right+1] = num_list[copy_right]
            copy_right -= 1
        
        num_list[left] = tmp

    return num_list


# ------------------------------------------------------
# 3. 希尔排序, 需要增量序列
# 希尔排序的思想是利用插入排序的优点，在数据量小、在数据量大致有序的情况下排序效率高
# ------------------------------------------------------


def shell_sort(num_list, step_seq=[5,3,1]):
    for step in step_seq:
        for i in range(step):
            copy_i = i
            seq_list = []
            while i<len(num_list):
                seq_list.append(num_list[i])
                i += step

            # 增量排序
            seq_list = insert_sort(seq_list)

            i = copy_i
            for index, num in enumerate(seq_list):
                num_list[index*step + i] = num

    return num_list



# ------------------------------------------------------
# 上面的属于插入排序，下面试一下交换排序，主要包括冒泡排序和快速排序
# ------------------------------------------------------

# ------------------------------------------------------
# 4. 冒泡排序
# ------------------------------------------------------


def bubble_sort(num_list):
    length = len(num_list)

    while length > 0:
        for i in range(length):
            if i>0 and num_list[i-1] > num_list[i]:
                num_list[i], num_list[i-1] = num_list[i-1], num_list[i]

        length -= 1 

    return num_list


# ------------------------------------------------------
# 5. 快速排序
# ------------------------------------------------------


# def quick_sort(num_list):
#     length = len(num_list)
#     if length <= 1:
#         return num_list

#     pivot = num_list[0]
#     left = 0
#     right = length - 1
#     rightflag = 1
#     for i in range(length - 1):
#         if rightflag:
#             if pivot < num_list[right]:
#                 right -= 1
#             else:
#                 num_list[left] = num_list[right]
#                 left += 1
#                 rightflag = 0
#         else:
#             if pivot >= num_list[left]:
#                 left += 1
#             else:
#                 num_list[right] = num_list[left]
#                 right -= 1
#                 rightflag = 1

#     num_list[left] = pivot
#     num_list[:left] = quick_sort(num_list[:left])
#     num_list[left+1:] = quick_sort(num_list[left+1:])
#     return num_list


def quick_sort(num_list, left, right):
    initial_left = left
    initial_right = right

    if left >= right:
        return

    pivot = num_list[left]
    while left < right and num_list[right] >= pivot:
        right -= 1
    num_list[left] = num_list[right]

    while left < right and num_list[left] <= pivot:
        left += 1
    num_list[right] = num_list[left]

    num_list[left] = pivot
    quick_sort(num_list, initial_left, left-1)
    quick_sort(num_list, left+1, initial_right)


# ------------------------------------------------------
# 6. 堆排序
    # num_list = ['', 49, 38, 65, 97, 76, 13, 27, 49]
    # small_heap_sort(num_list)
    # print(num_list)

    # ['', 97, 76, 65, 49, 49, 38, 27, 13]
# ------------------------------------------------------


# 调整堆
def adjust_heap(num_list, heap_len, i):
    mini = i
    left_index = 2*i
    right_index = 2*i + 1

    if left_index <= heap_len:
        left_node = num_list[left_index]
        if left_node < num_list[i]:
            mini = left_index

    if right_index <= heap_len:
        right_node = num_list[right_index]
        if right_node < left_node:
            mini = right_index
    
    if mini != i:
        num_list[mini], num_list[i] = num_list[i], num_list[mini]
        adjust_heap(num_list, heap_len, mini)


def small_heap_sort(num_list, heap_len):
    if heap_len <= 1:
        return

    # 创建小根堆，获取到最小的堆顶
    initail_len = heap_len//2
    while initail_len>0:
        adjust_heap(num_list, heap_len, initail_len)
        initail_len -= 1

    # 堆排序
    while heap_len>1:
        num_list[1], num_list[heap_len] = num_list[heap_len], num_list[1]
        heap_len -= 1
        adjust_heap(num_list, heap_len, 1)



# ------------------------------------------------------
# 7. 归并排序
# ------------------------------------------------------

def merge_2_list(num_list_1, num_list_2):
    ret_num_list = []

    while num_list_1 and num_list_2:
        if num_list_1[0] < num_list_2[0]:
            data = num_list_1.pop(0)
        else:
            data = num_list_2.pop(0)

        ret_num_list.append(data)

    if num_list_1:
        ret_num_list += num_list_1

    if num_list_2:
        ret_num_list += num_list_2

    return ret_num_list


def merge_sort(num_list):
    if len(num_list) < 2:
        return num_list

    left, right = 0, len(num_list) - 1
    mid = (left + right) // 2

    left_sort_list = merge_sort(num_list[:mid+1])
    right_sort_list = merge_sort(num_list[mid+1:])

    return merge_2_list(left_sort_list, right_sort_list)


if __name__ == '__main__':
    num_list = [49, 38, 65, 97, 76, 13, 27, 49]
    num_list = merge_sort(num_list)
    print(num_list)
    