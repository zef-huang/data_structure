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


# ------------------------------------------------------
# 2. 中序遍历的递归算法 (使用辅助栈)
# ------------------------------------------------------

def middle_visit_tree(root):
    stack = []
    p = root

    while p or stack:
        if p:
            stack.append(p)
            p = p.left
        else:
            p = stack.pop()
            print(p.data)
            p = p.right


# ------------------------------------------------------
# 3. 二叉树的层次遍历
# ------------------------------------------------------

import sys
sys.path.append('..')
from my_queue.loop_queue import LoopQueue

def level_order(root):
    queue = LoopQueue(100)
    queue.insert_ele(root)
    while queue:
        if not queue.get_size():
            print("二叉树层次遍历完成")
            break

        node = queue.get_ele()
        print(node.data)
        if node.left: 
            queue.insert_ele(node.left)
        if node.right: 
            queue.insert_ele(node.right)


if __name__ == '__main__':
    root = create_tree()
    level_order(root)
