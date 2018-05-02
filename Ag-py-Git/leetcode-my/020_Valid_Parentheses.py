# Given a string containing just the characters '(', ')', '{', '}', '[' and ']'
# determine if the input string is valid.
# The brackets must close in the correct order, "()" and "()[]{}" are all valid
# but "(]" and "([)]" are not.


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = ['()', '{}', '[]']
        s_stack = []
        for i in range(0, len(s)):
            s_stack.append(s[i])
            if len(s_stack) >= 2 and s_stack[-2] + s_stack[-1] in a:
                s_stack.pop
                s_stack.pop
        return len(s_stack) == 0
# 写染个函数最好写上起始与结束的值。只写结束值有可能会出错。
# 遇到配对检查的问题堆栈方法值得优先考虑。
