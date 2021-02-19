# coding=utf8


# ------------------------------------------------------
# 1. 二叉树先序遍历(二链结构)
# ------------------------------------------------------


class BtNode():
    left = None
    right = None

    def __init__(self, data):
        self.data = data


def create_tree():
    root = BtNode('A')
    node1 = BtNode('B')
    node2 = BtNode('C')
    node3 = BtNode('D')

    root.left = node1
    root.right = node2
    node1.right = node3

    return root


def pre_visit_tree(root):
    if not root:
        return
    
    print(root.data)
    pre_visit_tree(root.left)
    pre_visit_tree(root.right)


if __name__ == '__main__':
    root = create_tree()
    pre_visit_tree(root)
    
