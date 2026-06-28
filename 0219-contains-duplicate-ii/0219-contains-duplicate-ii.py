class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        lastSeen = {}

        for i, num in enumerate(nums):

            if num in lastSeen:

                if i - lastSeen[num] <= k:
                    return True

            lastSeen[num] = i

        return False      