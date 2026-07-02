class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        quotient = (dividend) // (divisor)
        if dividend < 0 and divisor > 0:
            quotient = -(abs(dividend) // abs(divisor))
        
        elif dividend > 0 and divisor < 0:
            quotient = -(abs(dividend) // abs(divisor))

        elif dividend < 0 and divisor < 0:
            quotient = abs(dividend) // abs(divisor)

        if quotient > pow(2,31)-1: 
            return quotient -1

        elif quotient < pow(-2,31): 
            return quotient

        return quotient