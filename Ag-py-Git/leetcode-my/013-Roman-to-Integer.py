# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans = 0
        for i in range(0, len(s)-1):
            num = s[i]
            numafter = s[i+1]
            if d[num] < d[numafter]:
                ans -= d[num]
            else:
                ans += d[num]
        return ans + d[s[-1]]
# 考虑罗马数字的规则即可。
