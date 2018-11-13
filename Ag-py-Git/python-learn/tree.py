# 二叉树的python学习
class Node():
    # 节点类定义
    def __init__(self, data=-1):
        self.data = data
        self.left = None
        self.right = None


class Tree():
    def __init__(self):
        self.root = Node()

    def add(self, data):
        # 添加树节点的方法，按照层次遍历的方式增长一棵树
        node = Node(data)
        if self.root.data == -1:
            self.root = node
        else:
            myqueue = []
            treeNode = self.root
            myqueue.append(treeNode)
            while myqueue:
                treeNode = myqueue.pop(0)
                if not treeNode.left:
                    treeNode.left = node
                    return
                elif not treeNode.right:
                    treeNode.right = node
                    return
                else:
                    myqueue.append(treeNode.left)
                    myqueue.append(treeNode.right)

    def pre_order(self, root):
        if not root:
            return
        print(root.data)
        self.pre_order(root.left)
        self.pre_order(root.right)

    def in_order(self, root):
        if not root:
            return
        self.in_order(root.left)
        print(root.data)
        self.in_order(root.right)

    def on_order(self, root):
        if not root:
            return
        self.on_order(root.left)
        self.on_order(root.right)
        print(root.data)


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tree = Tree()
    for i in data:
        tree.add(i)
    print('前序遍历')
    tree.pre_order(tree.root)
    print('中序遍历')
    tree.in_order(tree.root)
    print('后序遍历')
    tree.on_order(tree.root)
