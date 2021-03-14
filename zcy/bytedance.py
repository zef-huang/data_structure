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
# 2. 有个长度为 n 字符串，如果存在长度为 m 中子串各个字符都不一样，返回子串首个字符索引，否则返回 -1
# ------------------------------------------------------


def get_string_m_char_index(ss, n):
    ss_len = len(ss)
    if ss_len < n:
        return -1

    left = 0
    right = 0
    queue = []

    while right < ss_len:
        if (right - left) >= n:
            break

        while ss[right] in queue:
            queue.pop(0)
            left += 1

        queue.append(ss[right])
        right += 1      

    return left if left + n < ss_len else -1

if __name__ == '__main__':
    ss = 'sdhguahsdklighjosdih'
    index = get_string_m_char_index(ss, 12)
    print("index: ", index)