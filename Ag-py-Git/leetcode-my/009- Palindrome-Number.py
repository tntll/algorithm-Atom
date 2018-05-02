class Solution(object):
    def _isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = x
        revers = 0
        while x > 0:
            revers = revers*10 + x % 10
            x = x//10
        return temp == revers


class Solution2(object):
    def _isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        half = 0
        while x > half:
            half = half*10 + x % 10
            x = x//10
        return x == half or x == half//10
# 第二种方法似乎在时间复杂度上并没有多少下降。理论上来看是下降为n/2，但是提交后运行结果
# 证明反而更慢了。需要注意并不能使用python自带的str[::-1]这其实相当于违反了题目中要求的
# 不得使用额外空间。
