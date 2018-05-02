# Given a string, find the length of the longest substring without repeating
# characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the
# answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        start = 0
        ans = 0
        for i, str in enumerate(s):
            if str in d:
                start = max(start, d[str]+1)
            d[str] = i
            ans = max(ans, i-start+1)
        return ans
# 相当于设置一个从左开始的光标，来记录当前不重复子字符串的开头。然后根据依次添加入空字典的元素索引值与当前的光标值来的得到现有的子字符串长度，
# 如果比之前长就更新当前长度值。
