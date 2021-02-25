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

if __name__ == '__main__':
    num_list = [4, 2, 5, 7, 34, 3, 25, 67]
    sort_l = insert_sort(num_list)
    print(sort_l)
    