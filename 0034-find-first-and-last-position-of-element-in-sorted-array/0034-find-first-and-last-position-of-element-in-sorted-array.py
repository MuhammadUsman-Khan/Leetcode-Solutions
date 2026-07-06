class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            if nums[i] == target:
                j = i
                while j + 1 < len(nums) and nums[j + 1] == target:
                    j += 1
                return [i, j]
        return [-1,-1]