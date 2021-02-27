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

if __name__ == '__main__':
    num_list = [4, 2, 5, 7, 34, 3, 25, 67, 12]
    sort_l = bubble_sort(num_list)
    print(sort_l)
    