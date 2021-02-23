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


# -----------------------------------------------------
# 2. 二叉排序树建立
#              45
#             /  \
#            12  53
#           / \    \
#          3  37   100
#            /      /
#          24      61
#                   \
#                   90
#                   /
#                  78
# ------------------------------------------------------

class BiTreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create_bi_sorted_tree():
    root = BiTreeNode(45)
    node1 = BiTreeNode(12)
    node2 = BiTreeNode(3)
    node3 = BiTreeNode(37)
    node4 = BiTreeNode(24)

    node5 = BiTreeNode(53)
    node6 = BiTreeNode(100)
    node7 = BiTreeNode(61)
    node8 = BiTreeNode(90)
    node9 = BiTreeNode(78)

    root.left = node1
    node1.left = node2
    node1.right = node3
    node3.left = node4

    root.right = node5
    node5.right = node6
    node6.left = node7
    node7.right = node8
    node8.left = node9

    return root


# -----------------------------------------------------
# 2. 二叉排序树的中序遍历
# -----------------------------------------------------

def mid_visit_tree(root):

    if not root:
        return
    
    mid_visit_tree(root.left)
    print(root.data)
    mid_visit_tree(root.right)


def mid_visit_bi_sorted_tree():
    root = create_bi_sorted_tree()
    mid_visit_tree(root)


# -----------------------------------------------------
# 3. 二叉排序树的查找
# -----------------------------------------------------

def index_bi_sorted_tree(root, num):

    if not root:
        return None
    
    if root.data == num:
        return root

    if num < root.data:
        return index_bi_sorted_tree(root.left, num)
    else:
        return index_bi_sorted_tree(root.right, num)
    

if __name__ == '__main__':
    root = create_bi_sorted_tree()
    node = index_bi_sorted_tree(root, 112)
    if node:
        print(node.data)
    else:
        print("没有找到对应节点")
