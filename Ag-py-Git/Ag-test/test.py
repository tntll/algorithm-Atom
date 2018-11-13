a = [[1]]+[[2]]
print(a)
a = 13
print(a>>2)
a = '123123'
for i in a :
    print(i)
a = [1,3,2,4]
rowa = [i for i in a]
b = a.sort()
print(a)
print(rowa)
a = 2
b = 33
c = a^b
print(c)
c = c^b
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum < 3:
            return []
        small = 1
        big = 2
        res = []
        cursum = small+big
        mid = (tsum+1)>>1
        while small < mid:
            if cursum == tsum:
                res.append(list(range(small, big + 1)))
            elif cursum > tsum :
                cursum -= small
                small += 1
            elif cursum < tsum:
                cursum = cursum + big +1
                big = big+1
        return res
s = Solution()
print(s.FindContinuousSequence(10))
for i in range(1.0 5.5):
    print(i)
