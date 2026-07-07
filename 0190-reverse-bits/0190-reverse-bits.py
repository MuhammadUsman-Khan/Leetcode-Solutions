class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = bin(n)[2:].zfill(32)
        s = s[::-1]
        answer = int(s, 2)
        return answer