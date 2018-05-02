# Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        num = len(s)
        if num == 1:
            res = s
        result = {}
        for i in range(0, num):
            for j in range(i + 1, num):
                if s[i] == s[j]:
                    templen = 0
                    for k in range((j - i + 1) // 2 + 1):
                        if s[i + k] == s[j - k]:
                            templen += 1
                        if templen == ((j - i + 1) // 2 + 1):
                            result[j - i + 1] = s[i:j + 1]
        if result != {}:
            res = result.get(max(result.keys()))
        else:
            res = None
        return res

        # if len(s)==0:
        # 	return 0
        # maxLen=1
        # start=0
        # for i in range(len(s)):
        # 	if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
        # 		start=i-maxLen-1
        # 		maxLen+=2
        # 		continue
        # 	if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
        # 		start=i-maxLen
        # 		maxLen+=1
        # return s[start:start+maxLen]


class Solution1:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = '#'+'#'.join(s)+'#'

        RL = [0]*len(s)
        MaxRight = 0
        pos = 0
        MaxLen = 0
        for i in range(len(s)):
            if i < MaxRight:
                RL[i] = min(RL[2*pos-i], MaxRight-i)
            else:
                RL[i] = 1
            # 尝试扩展，注意处理边界
            while i-RL[i] >= 0 and i+RL[i] < len(s) and s[i-RL[i]] == s[i+RL[i]]:
                RL[i] += 1
            # 更新MaxRight,pos
            if RL[i]+i-1 > MaxRight:
                MaxRight = RL[i]+i-1
                pos = i
            # 更新最长回文串的长度
            MaxLen = max(MaxLen, RL[i])
        return MaxLen-1
