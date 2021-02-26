# coding=utf8


# ------------------------------------------------------
# 1. 插入排序
# ------------------------------------------------------


def insert_sort(num_list):
    for i in range(len(num_list)):
        tmp = num_list[i]
        while i>0 and num_list[i-1] > tmp:
            num_list[i] = num_list[i-1]
            i -= 1

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


if __name__ == '__main__':
    num_list = [4, 2, 5, 7, 34, 3, 25, 67, 12]
    sort_l = bi_insert_sort(num_list)
    print(sort_l)
    