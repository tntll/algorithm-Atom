# link-list
class SingleLinkList(object):

    # is_empty() 链表是否为空
    # length() 链表长度
    # travel() 遍历整个链表
    # add(item) 链表头部添加元素
    # append(item) 链表尾部添加元素
    # insert(pos, item) 指定位置添加元素
    # remove(item) 删除节点
    # search(item) 查找节点是否存在
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head == None

    def length(self):
        """链表长度"""
        # cur初始时指向头节点
        cur = self._head
        count = 0
        # 尾节点指向None，当未到达尾部时
        while cur != None:
            # if cur is not None:
            count += 1
            # 将cur后移一个节点
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self._head
        while cur != None:
            print(cur.item,)
            cur = cur.next
        print("")
