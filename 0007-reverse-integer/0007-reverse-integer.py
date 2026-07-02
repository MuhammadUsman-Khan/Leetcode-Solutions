class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x > 0:
            x = str(x)
            reversed_x = int(x[::-1])
        

        else:
            x = str(x)
            x = (x[0]) + x[:0:-1]
            reversed_x = int(x)
        
        if reversed_x > pow(2,31) or reversed_x < pow(-2,31):
            return 0

        return reversed_x