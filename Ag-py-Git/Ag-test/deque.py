# coding : utf-8

# 双端队列


class Deque(object):
    def __init__(self):
        self.__list = []
# Queue() 创建一个空的队列

    def add_front(self, item):
        # 往队列中添加一个item元素
        self.__list.insert(0, item)

    def add_rear(self, item):
        # 往队列中添加一个item元素
        self.__list.append(item)

    def pop_front(self):
        # 从队列头部删除一个元素
        return self.__list.pop(0)

    def pop_rear(self):
        # 从队列头部删除一个元素
        return self.__list.pop()

    def is_empty(self):
        # 判断一个队列是否为空
        return self.__list == []

    def size(self):
        # 返回队列的大小
        return len(self.__list)


if __name__ == '__main__':
    s = Deque()
    s.enqueue(1)
    s.enqueue(3)
    s.enqueue(5)
    print(s.dequeue())
    print(s.dequeue())
