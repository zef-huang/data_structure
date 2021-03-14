# coding=utf8


# ------------------------------------------------------
# 1. 有一棵后序遍历的树，请你恢复出原来的树结构, 并且返回头结点
# ------------------------------------------------------


class Node():
    left = None
    right = None

    def __init__(self, data):
        self.data = data


def post_order_bi_tree(root):
    if not root:
        return None

    if root.left:
        post_order_bi_tree(root.left)
    
    if root.right:
        post_order_bi_tree(root.right)

    print(root.data)

def get_tree_from_arry(num_list):
    if not num_list:
        return None
    
    slice = len(num_list) - 1
    while slice >= 0:
        if num_list[slice] < num_list[-1]:
            break
        slice -= 1

    left_tree = num_list[:slice + 1]
    right_tree = num_list[slice+1:-1]

    root = Node(num_list[-1])

    root.left = get_tree_from_arry(left_tree)
    root.right = get_tree_from_arry(right_tree)

    return root


# ------------------------------------------------------
# 2. 有个长度为 n 字符串，如果存在长度为 m 中目标子串(匹配字符可以和目标子串不一样，但是总的字符要一致)，返回子串首个字符索引，否则返回 -1
# ------------------------------------------------------


def get_string_m_char_index(ss, aims):
    n = len(ss)
    m = len(aims)
    aim_list = [i for i in aims]
    match_aim_list = []

    if n < m:
        return -1

    right = 0
    while right < n:
        if not aim_list:
            break

        if ss[right] in aim_list:
            pop_i = aim_list.index(ss[right])

            char = aim_list.pop(pop_i)
            match_aim_list.append(char)
        else:
            aim_list += match_aim_list
            match_aim_list = []

        right += 1

    return right - m if right <= n else -1


# ------------------------------------------------------
# 3. 最长无重复子子串长度
# ------------------------------------------------------


def get_longest_sub_string(ss):
    if not ss:
        return 0
    ss_len = len(ss)

    right = 0
    sub_str_max_len = 0
    queue = []
    while right < ss_len:
        while ss[right] in queue:
            queue.pop(0)

        queue.append(ss[right])
        sub_str_max_len = max(sub_str_max_len, len(queue))

        right += 1
    return sub_str_max_len


if __name__ == '__main__':
    ss = 'abcaac'
    length = get_longest_sub_string(ss)
    print("length: ", length)