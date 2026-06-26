class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        answerStart = 0
        answerEnd = 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return left + 1, right - 1

        for i in range(len(s)):

            start1, end1 = expand(i,i)

            start2, end2 = expand(i,i+1)


            if end1 - start1 > answerEnd - answerStart:
                answerStart = start1
                answerEnd = end1

            if end2 - start2 > answerEnd - answerStart:
                answerStart = start2
                answerEnd = end2

        return s[answerStart:answerEnd + 1]
        
        return substring