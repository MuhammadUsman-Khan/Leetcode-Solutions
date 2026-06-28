class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num1 = set(nums1)
        num2 = set(nums2)
        result = []
        for i in num1:
            for j in num2:
                if i == j:
                    result.append(i)

        return result