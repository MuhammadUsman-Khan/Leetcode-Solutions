class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        for i, letters in enumerate(zip(*strs)):
            if len(set(letters)) > 1:
                return strs[0][:i]

           
        return min(strs)