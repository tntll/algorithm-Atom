# 题目描述
# 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，
# 判断数组中是否含有该整数。


class Solution:
    # array 二维列表
    def Find(self, array, target):
        if array == [] or array == [[]]:
            return False
        row = len(array)
        col = len(array[0])
        for i in range(row-1, -1, -1):
            if target == array[i][0]:
                return True
                break
            if target > array[i][0]:
                for j in range(1, col-1):
                    if target == array[i][j]:
                        return True
                        break
            if i == 0:
                return False
