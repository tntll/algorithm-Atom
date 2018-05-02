# Reverse digits of an integer.
#
#
# Example1: x =  123, return  321
# Example2: x = -123, return -321


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            sign = -1
        else:
            sign = 1
        x = abs(x)
        ans = 0
        while x:
            ans = ans*10 + x % 10
            x = x//10
        return sign * ans if ans <= 0x7fffffff else 0
# 注意题目要求不能超过32位有符号整形数，超过就返回0。
# 32位有符号最大是31个1，所以用0x7fffffff正好表示。
