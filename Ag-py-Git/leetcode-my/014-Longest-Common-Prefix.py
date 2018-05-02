# Write a function to find the longest common prefix string amongst
# an array of strings.


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        i = 0
        j = 0
        end = 0
        while i < len(strs) and j < len(strs[i]):
            if i == 0:
                comstr = strs[i][j]
            else:
                if strs[i][j] != comstr:
                    break
            if i == len(strs) - 1:
                j += 1
                i = 0
                end += 1
            else:
                i += 1
        return strs[0][:end]
# 两个光标分别遍历每个str与每个str中的每一个字符。对于所有str从第一个字符开始比较是否
# 相同，如果相同则对所有的str进行下一个字符的比对。将相同的字符数记录下来即可。
