# 栈的实现（python）
# push（）添加元素到栈顶
# pop（）弹出栈顶元素
# peek（）返回栈顶元素
# size（）元素个数
# is_empty（）是否为空


class Stack(object):

    def __init__(self):
        self.__list = []

    def push(self, item):
        self.__list.append(item)

    def pop(self):
        return self.__list.pop()

    def peek(self):
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(3)
    s.push(5)
    print(s.pop())
    print(s.pop())
