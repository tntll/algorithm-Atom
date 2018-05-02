# Given a sorted array, remove the duplicates in place such that each
# element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this in


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minnum = 0
        if len(nums) <= 1:
            return len(nums)
        for i in range(1, len(nums)):
            if nums[i] != nums[minnum]:
                minnum += 1
                nums[minnum] = nums[i]
        return minnum+1
# 一般需要重新排列一个列表的时候都需要一个i遍历每个元素，另一个j来对当前需要判断的元素
# 进行标记，从而进行判断与位置变换。eeeeaaa
