# coding=utf8
# 使用 order_dict 实现一个 LRUCache

from collections import OrderedDict


class LRUCache():
    def __init__(self):
        self.op = OrderedDict()
        self.cap = 10

    def get(self, key):
        '''获取对应键的值, key 不存在时返回 None'''
        value = None
        if key in self.op:
            value = self.op[key]

        return value

    def set(self, key, value):
        '''设置对应键值对'''
        if key in self.op:
            self.op.move_to_end(key)
        else:
            if len(self.op) >= self.cap:
                self.op.pop_item(last=False)
            self.op[key] = value


if __name__ == "__main__":
    cache = LRUCache()
    
    for i in range(10):
        cache.set(str(i), i)
    
    print(cache.get('a'))
    print(cache.get('1'))
