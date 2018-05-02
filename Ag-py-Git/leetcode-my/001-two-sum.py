
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution(object):
    def twoSum(self, nums, target):
        '''
        type num:array
        type target:integer
        rtype :List
        '''
        # d = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    print([i, j])
                    return [i, j]


class Solution2(object):
    def twoSum(self, nums, target):
        '''
        type nums:array
        type target:integer
        rtype :List
        '''
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return[d[target - num], i]
            d[num] = i


if __name__ == '__main__':
    a = Solution()
    a.twoSum(nums=[2, 7, 11, 15], target=13)
