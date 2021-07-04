# coding=utf8
''' 使用 headp 获取 TOPK 个元素
    建立 K 个元素的堆，依次替换最小值
'''
import heapq


class TopK():
    def __init__(self, data_list, k):
        self.data_list = data_list
        self.k = k
        self.top_k_list = []

    def get_top_k(self):
        for num in self.data_list:
            self.push(num)
        
        return self.top_k_list
    
    def push(self, num):
        if len(self.top_k_list) >= self.k:
            val = self.top_k_list[0]
            if num < val:
                pass
            else:
                heapq.heapreplace(self.top_k_list, num)
        else:
            heapq.heappush(self.top_k_list, num)


if __name__ == '__main__':
    data_list = [i for i in range(10)]
    mgr = TopK(data_list, 3)
    top_k_list = mgr.get_top_k()
    print(top_k_list)
