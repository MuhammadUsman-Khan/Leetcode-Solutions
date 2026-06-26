class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        dup = sorted(set(nums))
        for num in dup:
            nums[k] = num
            k += 1
        return k
