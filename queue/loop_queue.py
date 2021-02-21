# coding=utf8


# ------------------------------------------------------
# 1. python 实现循环队列
# ------------------------------------------------------


class LoopQueue():
    def __init__(self, size):
        self.size = size
        self.p = 0
        self.queue = []

    def insert_ele(self, ele):
        if len(self.queue) >= self.size:
            raise Exception('队列已经满了')

        self.queue.insert(0, ele)

    def get_ele(self):
        if not len(self.queue):
            raise Exception("队列中没有元素了")

        return self.queue.pop()


def test_loop_queue():
    queue = LoopQueue(3)
    queue.insert_ele(11)        
    queue.insert_ele(22)        
    queue.insert_ele(33)
    print(queue.get_ele())        
    print(queue.get_ele())        
    print(queue.get_ele())        


if __name__ == '__main__':
    test_loop_queue()
    
        


